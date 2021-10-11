# pyright: reportUnknownVariableType=false

from typing import Union

from django.conf import settings
from django.contrib.auth.models import AnonymousUser, Group, User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.utils.translation import gettext_lazy as _

from .conf import NOSAVE, bcolors
from .hooks import dispatch
from .utils import get_admin_url, get_url, get_user

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", User)
SCOPE = (
    ("superuser", _("Superuser")),
    ("staff", _("Staff")),
    ("users", _("Users")),
    ("public", _("Public")),
)


class MEventManager(models.Manager):
    def create(self, *args, **kwargs):  # type: ignore
        keys = kwargs.keys()
        if "name" not in keys:
            raise ValueError("You must provide a 'name' argument for the MEvent")
        else:
            name = kwargs["name"]
        obj_pk: Union[int, None] = None
        if "obj_pk" in keys and "instance" not in keys:
            obj_pk = kwargs["obj_pk"]
        content_type = None
        model = None
        if "model" in keys and "instance" not in keys:
            model = kwargs["model"]
            content_type = ContentType.objects.get_for_model(model)
        # trying to grab an object instance in order to guess some fields
        instance: Union[Model, None] = None
        if obj_pk and content_type and "instance" not in keys:
            try:
                instance = content_type.get_object_for_this_type(pk=obj_pk)
            except Exception:
                pass
        if "instance" in keys:
            instance = kwargs["instance"]
            obj_pk = instance.pk  # type: ignore
            content_type = ContentType.objects.get_for_model(
                kwargs["instance"].__class__
            )
        # guessed stuff
        user = None
        if "user" in keys:
            user = kwargs["user"]
        else:
            if instance is not None:
                user = get_user(instance)
        url = ""
        if "url" in keys:
            url = kwargs["url"]
        else:
            if instance:
                url = get_url(instance)
        admin_url = ""
        if "admin_url" in keys:
            admin_url = kwargs["admin_url"]
        else:
            if instance:
                admin_url = get_admin_url(instance)
        # request
        formated_request = ""
        if "request" in keys:
            request = kwargs["request"]
            try:
                for key in request.META.keys():
                    formated_request += str(key) + " : " + str(request.META[key]) + "\n"
            except Exception:
                pass
        # static stuff
        event_class = ""
        if "event_class" in keys:
            event_class = kwargs["event_class"]
        notes = ""
        if "notes" in keys:
            notes = kwargs["notes"]
        if isinstance(user, AnonymousUser):
            user = None
        bucket = ""
        if "bucket" in keys:
            bucket = kwargs["bucket"]
        data = {}
        if "data" in keys:
            data = kwargs["data"]
        # scope
        scope = "superuser"
        if "scope" in keys:
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
        # create the event
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
            request=formated_request,
        )
        # add extra info from instance
        modelname = None
        if instance is not None:
            modelname = instance.__class__.__name__
        if model is not None:
            modelname = model.__name__
        if modelname is not None:
            if modelname in NOSAVE:
                return mevent
        # save by default unless it is said not to
        if "commit" in keys:
            if kwargs["commit"] is False:
                return mevent
        mevent.save(force_insert=True)
        # groups
        groups = None
        if "groups" in keys:
            groups = kwargs["groups"]
            mevent.groups.add(*groups)  # type: ignore
            mevent.save()
        # proceed hooks
        dispatch(mevent)
        # print info
        if settings.DEBUG:
            print(
                bcolors.SUCCESS
                + "Event"
                + bcolors.ENDC
                + " ["
                + str(mevent.event_class)
                + "] : "
                + name
            )
        return mevent

    def events_for_model(self, model, event_classes=[]):  # type: ignore
        content_type = ContentType.objects.get_for_model(model)
        if event_classes:
            qs = MEvent.objects.filter(
                content_type=content_type, event_class__in=event_classes
            )
        else:
            qs = MEvent.objects.filter(content_type=content_type)
        return qs

    def count_for_model(self, model, event_classes=[]):  # type: ignore
        content_type = ContentType.objects.get_for_model(model)
        if event_classes:
            qs = MEvent.objects.filter(
                content_type=content_type, event_class__in=event_classes
            ).count()
        else:
            qs = MEvent.objects.filter(content_type=content_type).count()
        return qs

    def events_for_object(self, obj):  # type: ignore
        content_type = ContentType.objects.get_for_model(obj.__class__)
        events = MEvent.objects.filter(content_type=content_type, obj_pk=obj.pk)
        return events


class MEvent(models.Model):
    # required fields
    content_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=True,
        verbose_name=_("Content type"),
        on_delete=SET_NULL,
    )
    obj_pk = models.IntegerField(
        blank=True, null=True, verbose_name=_("Object primary key")
    )
    name = models.CharField(max_length=120, verbose_name=_("Name"))
    # content fields
    url = models.CharField(max_length=255, blank=True, verbose_name=_("Url"))
    admin_url = models.CharField(
        max_length=255, blank=True, verbose_name=_("Admin url")
    )
    notes = models.TextField(blank=True)
    # meta
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name=_("Date posted"))
    event_class = models.CharField(max_length=120, blank=True, verbose_name=_("Class"))
    user = models.ForeignKey(
        USER_MODEL,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("User"),
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        verbose_name=_("Groups"),
    )
    request = models.TextField(blank=True, verbose_name=_("Request"))
    bucket = models.CharField(max_length=60, blank=True, verbose_name=_("Bucket"))
    data = models.TextField(blank=True, verbose_name=_("Data"))
    # manager
    scope = models.CharField(
        max_length=18,
        choices=SCOPE,
        default=SCOPE[0][0],
        verbose_name=_("Scope"),
    )
    objects = MEventManager()

    class Meta:  # type: ignore
        app_label = "mqueue"
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["-date_posted"]
        # permissions = (("view_mevent", "Can see Events"),)

    def __str__(self) -> str:
        return f"{self.name} - {self.date_posted}"
