# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType


class MEvent(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=_(u"Content type"))
    name = models.CharField(max_length=120, verbose_name=_(u"Name"))
    url = models.CharField(max_length=255, verbose_name=_(u"Url"))
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date posted"))
    obj_pk = models.IntegerField(verbose_name=_(u"Object primary key"))
    notes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = _(u'Events')
        verbose_name_plural = _(u'Events')
        ordering = ['-date_posted','name']
        
    def __unicode__(self):
        return self.name