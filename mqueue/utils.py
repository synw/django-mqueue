from django.urls import reverse
from .conf import (
    EVENT_CLASSES,
    EVENT_ICONS_HTML,
    EVENT_EXTRA_HTML,
    EVENT_DEFAULT_BADGES,
)


def get_event_class_str(event_class=None):
    event_class_str = "Default"
    if event_class is not None:
        if "created" in event_class:
            event_class_str = "Object created"
        if "deleted" in event_class:
            event_class_str = "Object deleted"
        if "edited" in event_class:
            event_class_str = "Object edited"
    return event_class_str


def get_event_badge(obj) -> str:
    """
    Get a badge html for an event
    """
    hasFormater = getattr(obj, "event_badge", None)
    if hasFormater:
        return obj.event_badge
    formated_event_class = get_event_class_str(obj.event_class)
    icon = EVENT_DEFAULT_BADGES["Default"]["icon"]
    name = obj.event_class
    if name is None:
        name = get_event_class_str(obj.event_class)
    if formated_event_class in EVENT_DEFAULT_BADGES.keys():
        icon = EVENT_DEFAULT_BADGES[formated_event_class]["icon"]
    html = '<span class="mq-label" style="">'
    icon_html = f'<i class="{icon}"></i>'
    html = icon_html + "&nbsp;" + name
    return html


def format_event_class(obj=None, event_class=None):
    event_html = ""
    if event_class is None:
        event_class = obj.event_class
    else:
        event_class = event_class
    printed_class = get_event_class_str(event_class).replace("_", " ").capitalize()
    icon = ""
    if event_class in EVENT_ICONS_HTML.keys():
        icon = EVENT_ICONS_HTML[event_class] + "&nbsp;"
        # printed_class = event_class
    else:
        event_class_lower = event_class.lower()
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
    if event_class in EVENT_EXTRA_HTML.keys():
        event_html += EVENT_EXTRA_HTML[event_class]
    return event_html


def get_object_name(instance, user):
    obj_name = ""
    try:
        obj_name = instance.__unicode__()
    except AttributeError:
        try:
            obj_name = instance.name
        except Exception:
            try:
                obj_name = instance.title
            except Exception:
                try:
                    obj_name = instance.slug
                except Exception:
                    obj_name = str(instance.pk)
    if obj_name:
        if len(obj_name) >= 45:
            obj_name = obj_name[:45] + "..."
    if hasattr(instance, "date_posted"):
        obj_name = instance.__class__.__name__ + " - " + str(instance.date_posted)
    elif hasattr(instance, "created"):
        obj_name = instance.__class__.__name__ + " - " + str(instance.created)
    if user:
        obj_name += " (" + user.username + ")"
    return obj_name


def get_user(instance):
    user = None
    try:
        user = instance.user
    except Exception:
        try:
            user = instance.editor
        except Exception:
            pass
    return user


def get_url(instance):
    url = ""
    get_event_object_url = getattr(instance.__class__, "get_event_object_url", None)
    if callable(get_event_object_url):
        url = instance.get_event_object_url()
        return url
    get_absolute_url = getattr(instance.__class__, "get_absolute_url", None)
    if callable(get_absolute_url):
        url = instance.get_absolute_url()
        return url
    return ""


def get_admin_url(instance):
    admin_url = reverse(
        "admin:%s_%s_change" % (instance._meta.app_label, instance._meta.model_name),
        args=[instance.id],
    )
    return admin_url
