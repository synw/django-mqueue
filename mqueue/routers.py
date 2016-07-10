# -*- coding: utf-8 -*-

"""
! NOT WORKING WHEN CONTENT TYPE IS NEEDED SOMEWHERE ELSE
TOFIX : do not use
"""


class MqueueLogRouter(object):
    """
    A router to control all database operations on models in
    the mqueue application
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on mqueue models to 'logs'
        """
        if model._meta.app_label == 'mqueue' or model._meta.app_label == 'content_type' :
            return 'logs'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'mqueue' or model._meta.app_label == 'content_type' :
            return 'logs'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure the 'mqueue' app only appears on the 'other' db
        """
        if db == 'logs':
            return model._meta.app_label == 'mqueue' or model._meta.app_label == 'content_type' 
        elif model._meta.app_label == 'mqueue' or model._meta.app_label == 'content_type' :
            return False
        return None
