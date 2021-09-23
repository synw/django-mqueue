import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from django.conf import settings
from .models import MEvent


class EventNode(DjangoObjectType):
    class Meta:
        model = MEvent
        only_fields = ("name", "event_class", "url", "date_posted", "data")
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "event_class": ["exact", "icontains", "istartswith"],
            "date_posted": ["exact", "icontains", "istartswith"],
            "bucket": ["exact", "icontains", "istartswith"],
        }
        interfaces = (relay.Node,)


class StaffEventNode(DjangoObjectType):
    class Meta:
        model = MEvent
        only_fields = (
            "name",
            "event_class",
            "url",
            "date_posted",
            "data",
            "admin_url",
        )
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "event_class": ["exact", "icontains", "istartswith"],
            "date_posted": ["exact", "icontains", "istartswith"],
            "bucket": ["exact", "icontains", "istartswith"],
        }
        interfaces = (relay.Node,)


class SuperuserEventNode(DjangoObjectType):
    class Meta:
        model = MEvent
        only_fields = (
            "name",
            "event_class",
            "url",
            "date_posted",
            "data",
            "admin_url",
            "request",
            "notes",
            "bucket",
            "obj_pk",
        )
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "event_class": ["exact", "icontains", "istartswith"],
            "date_posted": ["exact", "icontains", "istartswith"],
            "bucket": ["exact", "icontains", "istartswith"],
        }
        interfaces = (relay.Node,)


class EQuery(graphene.AbstractType):
    public_events = DjangoFilterConnectionField(EventNode)
    users_events = DjangoFilterConnectionField(EventNode)
    staff_events = DjangoFilterConnectionField(StaffEventNode)
    all_events = DjangoFilterConnectionField(SuperuserEventNode)

    def resolve_public_events(root, info, **kwargs):  # type: ignore
        return MEvent.objects.filter(scope="public")

    def resolve_users_events(root, info, **kwargs):  # type: ignore
        if info.context.user.is_authenticated:
            return MEvent.objects.filter(scope="users")
        return MEvent.objects.none()

    def resolve_staff_events(root, info, **kwargs):  # type: ignore
        if info.context.user.is_staff:
            return MEvent.objects.filter(scope="staff")
        return MEvent.objects.none()

    def resolve_all_events(root, info, **kwargs):  # type: ignore
        if info.context.user.is_superuser:
            return MEvent.objects.all()
        return MEvent.objects.none()


class Query(EQuery, graphene.ObjectType):
    if settings.DEBUG is True:
        debug = graphene.Field(DjangoDebug, name="__debug")
    else:
        pass


schema = graphene.Schema(query=Query)
