from typing import Union

from django.contrib.auth.models import User
from django.db.models.base import Model
from django.urls import reverse

from .conf import (
    EVENT_CLASSES,
    EVENT_DEFAULT_BADGES,
    EVENT_EXTRA_HTML,
    EVENT_ICONS_HTML,
)


def get_event_class_str(event_class: Union[str, None] = None) -> str:
    event_class_str = "Default"
    if event_class is not None:
        if "created" in event_class:
            event_class_str = "Object created"
        if "deleted" in event_class:
            event_class_str = "Object deleted"
        if "edited" in event_class:
            event_class_str = "Object edited"
    return event_class_str


def get_event_badge(obj) -> str:  # type: ignore
    """
    Get a badge html for an event
    """
    hasFormater = getattr(obj, "event_badge", None)
    if hasFormater:
        return obj.event_badge  # type: ignore
    formated_event_class = get_event_class_str(str(obj.event_class))
    icon = EVENT_DEFAULT_BADGES["Default"]["icon"]
    name: str = str(obj.event_class)
    if name is None:
        name = get_event_class_str(str(obj.event_class))
    if formated_event_class in EVENT_DEFAULT_BADGES.keys():
        icon = EVENT_DEFAULT_BADGES[formated_event_class]["icon"]
    html = '<span class="mq-label" style="">'
    icon_html = f'<i class="{icon}"></i>'
    html = icon_html + "&nbsp;" + name
    return html


def format_event_class(
    obj=None, event_class: Union[str, None] = None  # type: ignore
) -> str:
    event_html = ""
    if event_class is None:
        _event_class: str = obj.event_class  # type: ignore
    else:
        _event_class = event_class
    printed_class = get_event_class_str(event_class).replace("_", " ").capitalize()
    icon = ""
    if _event_class in EVENT_ICONS_HTML.keys():
        icon = EVENT_ICONS_HTML[_event_class] + "&nbsp;"
        # printed_class = event_class
    else:
        event_class_lower = _event_class.lower()
        if "created" in event_class_lower:
            icon = EVENT_ICONS_HTML["Object created"] + "&nbsp;"
            printed_class = "Object created"
        elif "edited" in event_class_lower:
            icon = EVENT_ICONS_HTML["Object edited"] + "&nbsp;"
            printed_class = "Object edited"
        elif "deleted" in event_class_lower:
            icon = EVENT_ICONS_HTML["Object deleted"] + "&nbsp;"
            printed_class = "Object deleted"
        else:
            icon = EVENT_ICONS_HTML["Default"] + "&nbsp;"
            printed_class = "Default"
        if "error" in event_class_lower:
            icon = EVENT_ICONS_HTML["Error"] + "&nbsp;"
            printed_class = "Error"
        elif "debug" in event_class_lower:
            icon = EVENT_ICONS_HTML["Debug"] + "&nbsp;"
            printed_class = "Debug"
        elif "warning" in event_class_lower:
            icon = EVENT_ICONS_HTML["Warning"] + "&nbsp;"
            printed_class = "Warning"
        elif "info" in event_class_lower or "infos" in event_class_lower:
            icon = EVENT_ICONS_HTML["Info"] + "&nbsp;"
            printed_class = "Info"
        elif "important" in event_class_lower:
            icon = EVENT_ICONS_HTML["Important"] + "&nbsp;"
            printed_class = "Important"
    event_html += (
        '<span class="'
        + EVENT_CLASSES[printed_class]
        + '">'
        + icon
        + printed_class
        + "</span>"
    )
    if _event_class in EVENT_EXTRA_HTML.keys():
        event_html += EVENT_EXTRA_HTML[_event_class]
    return event_html


def get_object_name(instance: Model, user: User) -> str:
    obj_name: str = ""
    try:
        obj_name = instance.__str__()  # type: ignore
    except AttributeError:
        try:
            obj_name = instance.name  # type: ignore
        except Exception:
            try:
                obj_name = instance.title  # type: ignore
            except Exception:
                try:
                    obj_name = instance.slug  # type: ignore
                except Exception:
                    obj_name = str(instance.pk)
    if obj_name:
        if len(obj_name) >= 45:
            obj_name = obj_name[:45] + "..."
    if hasattr(instance, "date_posted"):
        obj_name = instance.__class__.__name__ + " - "
        obj_name += str(instance.date_posted)  # type: ignore
    elif hasattr(instance, "created"):
        obj_name = instance.__class__.__name__ + " - "
        obj_name += (str(instance.created),)  # type: ignore
    if user:
        obj_name += f" ({user.username})"
    return obj_name


def get_user(instance: Model) -> Union[User, None]:
    user: Union[User, None] = None
    try:
        user = instance.user  # type: ignore
    except Exception:
        try:
            user = instance.editor  # type: ignore
        except Exception:
            pass
    return user


def get_url(instance: Model) -> str:
    url = ""
    get_event_object_url = getattr(instance.__class__, "get_event_object_url", None)
    if callable(get_event_object_url):
        url = instance.get_event_object_url()  # type: ignore
        return url  # type: ignore
    get_absolute_url = getattr(instance.__class__, "get_absolute_url", None)
    if callable(get_absolute_url):
        url = instance.get_absolute_url()  # type: ignore
        return url  # type: ignore
    return ""


def get_admin_url(instance: Model) -> str:
    admin_url = reverse(
        "admin:%s_%s_change"
        % (instance._meta.app_label, instance._meta.model_name),  # type: ignore
        args=[instance.id],  # type: ignore
    )
    return admin_url
