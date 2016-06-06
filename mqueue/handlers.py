# -*- coding: utf-8 -*-

from logging import Handler
from django.conf import settings
import traceback

 
class LogsDBHandler(Handler,object):
 
    def emit(self,record):
        from mqueue.models import MEvent
        msg = record.getMessage()
        name= msg
        if record.exc_info:
            ex_type = repr((record.exc_info[0]))
            ex_title =  repr(record.exc_info[1])
            ex_traceback = '\n'.join(traceback.format_tb(record.exc_info[2]))
            msg+='\n\n'+ex_title+'\n\n'+ex_type+'\n\n'+ex_traceback
        if settings.DEBUG is True:
            event_class = 'Dev log '+record.levelname
        else:
            event_class = 'Log '+record.levelname
        MEvent.objects.create(
                              name=name, 
                              event_class=event_class, 
                              notes=msg, 
                              user=record.request.user, 
                              request=record.request,
                              url=record.request.path,
                              )
        return

