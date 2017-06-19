import importlib
from mqueue.conf import HOOKS

def dispatch(event):
    for hook in HOOKS:
        path = "mqueue.hooks."+hook
        module = importlib.import_module(path)
        func = getattr(module, "Save")
        func(event)