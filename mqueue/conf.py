from typing import Dict, List
from django.conf import settings


WATCH: List[str] = getattr(settings, "MQUEUE_WATCH", [])

NOSAVE: List[str] = getattr(settings, "MQUEUE_NOSAVE", [])

HOOKS: Dict[str, Dict[str, str | int]] = getattr(settings, "MQUEUE_HOOKS", {})

DOMAIN = getattr(settings, "SITE_SLUG", "default")

API_MAX_EVENTS = getattr(settings, "MQUEUE_API_MAX_EVENTS", 100)

# ===================== Events formats ===================================
EVENT_CLASSES = {
    # 'Event class label': 'css class to apply',
    "Default": "mq-label mq-default",
    "Important": "mq-label mq-important",
    "Ok": "mq-label mq-ok",
    "Info": "mq-label mq-info",
    "Debug": "mq-label mq-debug",
    "Warning": "mq-label mq-warning",
    "Error": "mq-label mq-error",
    "Object created": "mq-label mq-created",
    "Object edited": "mq-label mq-edited",
    "Object deleted": "mq-label mq-deleted",
}

EVENT_CLASSES = getattr(settings, "MQUEUE_EVENT_CLASSES", EVENT_CLASSES)

EVENT_ICONS_HTML = {
    # 'Event class label': 'icon css class',
    "Default": '<i class="fa fa-flash"></i>',
    "Important": '<i class="fa fa-exclamation"></i>',
    "Ok": '<i class="fa fa-thumbs-up"></i>',
    "Info": '<i class="fa fa-info-circle"></i>',
    "Debug": '<i class="fa fa-cog"></i>',
    "Warning": '<i class="fa fa-exclamation"></i>',
    "Error": '<i class="fa fa-exclamation-triangle"></i>',
    "Object edited": '<i class="fa fa-pencil"></i>',
    "Object created": '<i class="fa fa-plus"></i>',
    "Object deleted": '<i class="fa fa-remove"></i>',
}

EVENT_ICONS_HTML = getattr(settings, "MQUEUE_EVENT_ICONS_HTML", EVENT_ICONS_HTML)

EVENT_EXTRA_HTML: Dict[str, str] = getattr(settings, "MQUEUE_EVENT_EXTRA_HTML", {})

EVENT_DEFAULT_BADGES = {
    "Default": {
        "css": {"background-color": "firebrick", "color": "white"},
        "icon": "fa fa-flash",
    },
    "Important": {
        "css": {"background-color": "firebrick", "color": "white"},
        "icon": "fa fa-exclamation",
    },
    "Ok": {
        "css": {"background-color": "forestgreen", "color": "white"},
        "icon": "fa fa-thumbs-up",
    },
    "Info": {
        "css": {"background-color": "royalblue", "color": "white"},
        "icon": "fa fa-info-circle",
    },
    "Debug": {
        "css": {"background-color": "orange", "color": "black"},
        "icon": "fa fa-cog",
    },
    "Warning": {
        "css": {"background-color": "yellow", "color": "black"},
        "icon": "fa fa-exclamation",
    },
    "Error": {
        "css": {"background-color": "red", "color": "black"},
        "icon": "fa fa-exclamation-triangle",
    },
    "Object created": {
        "css": {"background-color": "darkcyan", "color": "white"},
        "icon": "fa fa-plus",
    },
    "Object edited": {
        "css": {"background-color": "dodgerblue", "color": "white"},
        "icon": "fa fa-pencil",
    },
    "Object deleted": {
        "css": {"background-color": "lightcoral", "color": "white"},
        "icon": "fa fa-remove",
    },
}

# ===================== Websocket stream ===================================

# terminal output colors


class bcolors:
    HEADER = "\033[95m"
    PRIMARY = "\033[94m"
    SUCCESS = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
