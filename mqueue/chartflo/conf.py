# -*- coding: utf-8 -*-
from dataswim import ds
from .gen_conf import dburl, datapath, report_path


def init():
    ds.datapath = datapath
    ds.report_path = report_path
    ds.connect(dburl)
