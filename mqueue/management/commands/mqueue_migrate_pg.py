from __future__ import print_function
import os
from django.core.management.base import BaseCommand
from mqueue.hooks import postgresql
from mqueue.conf import HOOKS


class Command(BaseCommand):
    help = 'Migrates a postgresql database for mqueue hook'

    def handle(self, *args, **options):
        # verify config
        if "postgresql" not in HOOKS:
            print("No postgresql database configured: please check HOOKS in settings")
        conf = HOOKS["postgresql"]
        # run
        params = ["-a=" + conf["addr"]]
        params.append('-du="' + conf["user"] + '"')
        params.append('-p="' + conf["password"] + '"')
        params.append('-d="' + conf["database"] + '"')
        params.append("-m")
        pth = os.path.dirname(postgresql.__file__)
        cmd = pth + "/run " + str.join(" ", params)
        os.system(cmd)
        return
