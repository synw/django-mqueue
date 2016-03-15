# -*- coding: utf-8 -*-

from django.conf import settings
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from causer.models import Forum, Topic, Post


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'status']
        widgets = {'status': forms.RadioSelect}
        

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'forum', 'status', 'monitoring_level', 'event_class', 'posted_by']
        widgets = {'status': forms.RadioSelect, 'monitoring_level': forms.RadioSelect}
       
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'topic', 'content', 'status', 'event_class', 'posted_by']
        widgets = {'status': forms.RadioSelect}
        

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    form = ForumForm
    date_hierarchy = 'edited'
    readonly_fields = [ 'num_topics', 'total_posts', 'editor', 'edited', 'created' ]
    list_display = ['title', 'num_topics', 'total_posts', 'status', 'editor', 'edited']
    list_filter = ['status']
    search_fields = ['title', 'editor__username']
    
    def save_model(self, request, obj, form, change):
        obj.editor = request.user
        super(ForumAdmin, self).save_model(request, obj, form, change)
    

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    form = TopicForm
    date_hierarchy = 'edited'
    readonly_fields = [ 'num_posts', 'num_views', 'editor', 'edited', 'created' ]
    list_display = ['title', 'forum', 'num_posts', 'num_views', 'status', 'monitoring_level', 'editor', 'edited']
    list_filter = ['status']
    search_fields = ['title', 'editor__username']
    
    def save_model(self, request, obj, form, change):
        obj.editor = request.user
        super(TopicAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    date_hierarchy = 'edited'
    readonly_fields = [ 'editor', 'edited', 'created' ]
    list_display = ['title', 'topic', 'status', 'monitoring_level', 'editor', 'edited']
    list_filter = ['status', 'topic__title']
    search_fields = ['title', 'editor__username', 'topic__title']
    
    def save_model(self, request, obj, form, change):
        obj.editor = request.user
        obj.save()
        super(PostAdmin, self).save_model(request, obj, form, change)
        
        
        
        
        
