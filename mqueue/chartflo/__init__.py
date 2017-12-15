from .transform import run as transform
from .home import run as home
from .conf import init


def run(**kwargs):
    init()
    #transform()
    home()
