# -*- coding: utf-8 -*-

import traceback
from logging import Handler


class LogsDBHandler(Handler,object):
 
    def emit(self,record):
        from mqueue.models import MEvent
        msg = record.getMessage()
        name= msg[:120]
        if record.exc_info:
            ex_type = repr((record.exc_info[0]))
            ex_title =  repr(record.exc_info[1])
            ex_traceback = '\n'.join(traceback.format_tb(record.exc_info[2]))
            msg+='\n\n'+ex_title+'\n\n'
            msg += ex_type
            msg += '\n\n'+ex_traceback
        event_class = 'Log '+record.levelname
        try:
            user = record.request.user
        except:
            user = None
        path = ""
        try:
            path = record.request.path
        except:
            pass
        if user is not None:
            MEvent.objects.create(
                                  name=name, 
                                  event_class=event_class, 
                                  notes=msg, 
                                  user=user, 
                                  request=record.request,
                                  url=path,
                                  )
        else:
            MEvent.objects.create(
                                  name=name, 
                                  event_class=event_class, 
                                  notes=msg, 
                                  request=record.request,
                                  url=path,
                                  )
        return

