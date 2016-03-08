# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType


class ModerationEvent(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name="Content type")
    name = models.CharField(max_length=120, verbose_name="Name")
    url = models.CharField(max_length=255, verbose_name='Url')
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Date posted")
    obj_pk = models.IntegerField(verbose_name='Object primary key')
    notes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Moderation event'
        verbose_name_plural = 'Moderation events'
        ordering = ['-date_posted','name']
        
    def __unicode__(self):
        return self.name
