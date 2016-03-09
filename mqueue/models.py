# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType


WARN_ON=getattr(settings, 'MQUEUE_WARN_ON', 'warning')


class MEventManager(models.Manager):
    def create(self, *args, **kwargs):
        if not 'name' in kwargs.keys():
            raise ValueError(u"You must provide a 'name' argument for the MEvent")
        else:
            name = kwargs['name']
        if not 'model' in kwargs.keys():
            raise ValueError(u"You must provide a 'model' argument for the MEvent")
        else:
            content_type = ContentType.objects.get_for_model(kwargs['model'])
        if not 'obj_pk' in kwargs.keys():
            raise ValueError(u"You must provide an 'obj_pk' argument for the MEvent")
        else:
            obj_pk = kwargs['obj_pk'] 
        notes = ''
        if 'notes' in kwargs.keys():
            notes = kwargs['notes']
        url = ''
        if 'url' in kwargs.keys():
            url = kwargs['url']
        admin_url = ''
        if 'admin_url' in kwargs.keys():
            admin_url = kwargs['admin_url']
        event_class = ''
        if 'event_class' in kwargs.keys():
            event_class = kwargs['event_class']
        mevent = MEvent(name=name, content_type=content_type, obj_pk=obj_pk, url=url, admin_url=admin_url, notes=notes, event_class=event_class)
        mevent.save(force_insert=True)
        return mevent


class MEvent(models.Model):
    #~ required fields
    content_type = models.ForeignKey(ContentType, verbose_name=_(u"Content type"))
    obj_pk = models.IntegerField(verbose_name=_(u"Object primary key"))
    name = models.CharField(max_length=120, verbose_name=_(u"Name"))
    #~ content fields
    url = models.CharField(max_length=255, blank=True, verbose_name=_(u"Url"))
    admin_url = models.CharField(max_length=255, blank=True, verbose_name=_(u"Admin url"))
    notes = models.TextField(blank=True)
    #~ meta
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date posted"))
    event_class = models.CharField(max_length=120, blank=True, verbose_name=_(u"Class"))
    #~ manager
    events = MEventManager()
    
    class Meta:
        verbose_name = _(u'Events')
        verbose_name_plural = _(u'Events')
        ordering = ['-date_posted', 'event_class', 'name']
        
    def __unicode__(self):
        return self.name
    
    
        
        
        
