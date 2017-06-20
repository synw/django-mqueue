import importlib
from mqueue.conf import HOOKS

def dispatch(event):
    for name in HOOKS:
        hook = HOOKS[name]
        path = hook["path"]
        module = importlib.import_module(path)
        func = getattr(module, "Save")
        func(event, hook)
