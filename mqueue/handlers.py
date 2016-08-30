# -*- coding: utf-8 -*-

import traceback
from logging import Handler
from django.conf import settings
from mqueue.conf import LIVE_FEED
if LIVE_FEED is True:
    from mqueue_livefeed.conf import STREAM_LOGS, CHANNEL
    from instant import broadcast


class LogsDBHandler(Handler,object):
 
    def emit(self,record):
        from mqueue.models import MEvent
        msg = record.getMessage()
        name= msg[:120]
        if record.exc_info:
            ex_type = repr((record.exc_info[0]))
            ex_title =  repr(record.exc_info[1])
            ex_traceback = '\n'.join(traceback.format_tb(record.exc_info[2]))
            msg+='\n\n'+ex_title+'\n\n'+ex_type+'\n\n'+ex_traceback
        if settings.DEBUG is True:
            event_class = 'Dev log '+record.levelname
        else:
            event_class = 'Log '+record.levelname
        try:
            user = record.request.user
        except:
            user = None
        if user is not None:
            MEvent.objects.create(
                                  name=name, 
                                  event_class=event_class, 
                                  notes=msg, 
                                  user=user, 
                                  request=record.request,
                                  url=record.request.path,
                                  )
        else:
            MEvent.objects.create(
                                  name=name, 
                                  event_class=event_class, 
                                  notes=msg, 
                                  request=record.request,
                                  url=record.request.path,
                                  )
        if LIVE_FEED is True and STREAM_LOGS is True:
            broadcast(message=name, event_class=event_class, channel=CHANNEL)
        return

