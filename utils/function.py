# -*- coding: utf-8 -*-
import hashlib

def md5_encode(str):
    u"""
    summary:
        MD5 encode
    """
    return hashlib.md5(str.encode("utf-8")).hexdigest()

def get_referer_url(request):
    """
    summary:
        get request referer url address,default /
    """
    return request.META.get('HTTP_REFERER', '/')