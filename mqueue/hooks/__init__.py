import importlib
from mqueue.conf import HOOKS


def dispatch(event):
    for name in HOOKS:
        hook = HOOKS[name]
        path = hook["path"]
        module = importlib.import_module(f"{path}")
        func = getattr(module, "save")
        func(event, hook)
