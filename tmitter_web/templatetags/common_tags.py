# -*- coding: utf-8 -*-
from django.template import Library
from tmitter_web.models import *
from tmitter.settings import *

register = Library()


def in_list(val, lst):
    """
    summary:
        检查只时候在列表中
    """
    return val in lst


def replace(content):
    """
        replaces:
            替换
        """
    content.replace('\n', '')


register.filter("in_list", in_list)
register.filter("replace", replace)
