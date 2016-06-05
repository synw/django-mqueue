# -*- coding: utf-8 -*-

import traceback
from logging import Handler
from django.conf import settings
from django.contrib.auth import get_user

 
class LogsDBHandler(Handler,object):
 
    def emit(self,record):
        from mqueue.models import MEvent
        msg = record.getMessage()
        name= msg
        if record.exc_info:
            ex_type = str(record.exc_info[0])
            ex_title =  str(record.exc_info[1])
            ex_traceback = '\n'.join(traceback.format_tb(record.exc_info[2]))
            msg+='\n\n'+ex_title+'\n\n'+ex_type+'\n\n'+ex_traceback
        if settings.DEBUG is True:
            event_class = 'Dev log '+record.levelname
        else:
            event_class = 'Log '+record.levelname
        user=get_user(record.request)
        from django.contrib.auth.models import AnonymousUser
        if isinstance(user, AnonymousUser):
            user = None
        MEvent.objects.create(
                              name=name, 
                              event_class=event_class, 
                              notes=msg, 
                              user=user, 
                              request=record.request,
                              url=record.request.path,
                              )
        return

