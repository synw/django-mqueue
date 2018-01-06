# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, AnonymousUser
from mqueue.utils import get_user, get_url, get_admin_url
from mqueue.hooks import dispatch
from mqueue.conf import bcolors, NOSAVE


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)
SCOPE = (
    ('superuser', _('Superuser')),
    ('staff', _('Staff')),
    ('users', _('Users')),
    ('public', _('Public')),
)


class MEventManager(models.Manager):
    def create(self, *args, **kwargs):
        if 'name' not in kwargs.keys():
            raise ValueError(
                u"You must provide a 'name' argument for the MEvent")
        else:
            name = kwargs['name']
        obj_pk = None
        if 'obj_pk' in kwargs.keys() and 'instance' not in kwargs.keys():
            obj_pk = kwargs['obj_pk']
        content_type = None
        model = None
        if 'model' in kwargs.keys() and 'instance' not in kwargs.keys():
            model = kwargs['model']
            content_type = ContentType.objects.get_for_model(model)
        # trying to grab an object instance in order to guess some fields
        instance = None
        if obj_pk and content_type and 'instance' not in kwargs.keys():
            try:
                instance = content_type.get_object_for_this_type(pk=obj_pk)
            except Exception:
                pass
        if 'instance' in kwargs.keys():
            instance = kwargs['instance']
            obj_pk = instance.pk
            content_type = ContentType.objects.get_for_model(
                kwargs['instance'].__class__)
        # guessed stuff
        user = None
        if 'user' in kwargs.keys():
            user = kwargs['user']
        else:
            if instance:
                user = get_user(instance)
        url = ''
        if 'url' in kwargs.keys():
            url = kwargs['url']
        else:
            if instance:
                url = get_url(instance)
        admin_url = ''
        if 'admin_url' in kwargs.keys():
            admin_url = kwargs['admin_url']
        else:
            if instance:
                admin_url = get_admin_url(instance)
        # request
        save_request = False
        if 'request' in kwargs.keys():
            request = kwargs['request']
            formated_request = ''
            try:
                for key in request.META.keys():
                    formated_request += str(key) + ' : ' + \
                        str(request.META[key]) + '\n'
                save_request = True
            except Exception:
                pass
        # static stuff
        event_class = ''
        if 'event_class' in kwargs.keys():
            event_class = kwargs['event_class']
        notes = ''
        if 'notes' in kwargs.keys():
            notes = kwargs['notes']
        if isinstance(user, AnonymousUser):
            user = None
        bucket = ""
        if 'bucket' in kwargs.keys():
            bucket = kwargs["bucket"]
        data = {}
        if "data" in kwargs.keys():
            data = kwargs["data"]
        # scope
        scope = "superuser"
        if "scope" in kwargs.keys():
            scope = kwargs["scope"]
            # test if it is an allowed scope
            isok = False
            for s in SCOPE:
                if s[0] == scope:
                    isok = True
                    break
            if isok is False:
                msg = "Unable to create event: wrong scope provided: \
                choices are: superuser, staff, users, public"
                MEvent.objects.create(name=msg, event_class="Error")
                return None
        # create te event
        mevent = MEvent(
            name=name,
            content_type=content_type,
            obj_pk=obj_pk,
            user=user,
            url=url,
            admin_url=admin_url,
            notes=notes,
            event_class=event_class,
            bucket=bucket,
            data=data,
            scope=scope,
        )
        if save_request is True:
            mevent.request = formated_request
        # proceed hooks
        dispatch(mevent)
        # print info
        if settings.DEBUG:
            print(bcolors.SUCCESS + 'Event' + bcolors.ENDC +
                  ' [' + mevent.event_class + '] : ' + name)
        # save by default unless it is said not to
        modelname = None
        if instance is not None:
            modelname = instance.__class__.__name__
        if model is not None:
            modelname = model.__name__
        if modelname is not None:
            if modelname in NOSAVE:
                return mevent
        if 'commit' in kwargs.keys():
            if kwargs['commit'] is False:
                return mevent
        mevent.save(force_insert=True)
        return mevent

    def events_for_model(self, model, event_classes=[]):
        content_type = ContentType.objects.get_for_model(model)
        if event_classes:
            qs = MEvent.objects.filter(
                content_type=content_type, event_class__in=event_classes)
        else:
            qs = MEvent.objects.filter(content_type=content_type)
        return qs

    def count_for_model(self, model, event_classes=[]):
        content_type = ContentType.objects.get_for_model(model)
        if event_classes:
            qs = MEvent.objects.filter(
                content_type=content_type, event_class__in=event_classes).count()
        else:
            qs = MEvent.objects.filter(content_type=content_type).count()
        return qs

    def events_for_object(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        events = MEvent.objects.filter(
            content_type=content_type, obj_pk=obj.pk)
        return events


class MEvent(models.Model):
    # required fields
    content_type = models.ForeignKey(
        ContentType, null=True, blank=True, verbose_name=_(u"Content type"))
    obj_pk = models.IntegerField(
        blank=True, null=True, verbose_name=_(u"Object primary key"))
    name = models.CharField(max_length=120, verbose_name=_(u"Name"))
    # content fields
    url = models.CharField(max_length=255, blank=True, verbose_name=_(u"Url"))
    admin_url = models.CharField(
        max_length=255, blank=True, verbose_name=_(u"Admin url"))
    notes = models.TextField(blank=True)
    # meta
    date_posted = models.DateTimeField(
        auto_now_add=True, verbose_name=_(u"Date posted"))
    event_class = models.CharField(
        max_length=120, blank=True, verbose_name=_(u"Class"))
    user = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='+',
                             on_delete=models.SET_NULL, verbose_name=_(u'User'))
    request = models.TextField(blank=True, verbose_name=_(u'Request'))
    bucket = models.CharField(
        max_length=60, blank=True, verbose_name=_(u"Bucket"))
    data = models.TextField(blank=True, verbose_name=_(u"Data"))
    # manager
    scope = models.CharField(max_length=18, choices=SCOPE,
                             default=SCOPE[0][0], verbose_name=_(u"Scope"))
    objects = MEventManager()

    class Meta:
        app_label = 'mqueue'
        verbose_name = _(u'Event')
        verbose_name_plural = _(u'Events')
        ordering = ['-date_posted']
        permissions = (("view_mevent", "Can see Events"),)

    def __unicode__(self):
        return self.name + ' - ' + str(self.date_posted)
