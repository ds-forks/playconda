#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: urls.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-04-30
"""

from django.conf.urls import url

from playconda.core.views import index, search, details

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^search$', search, name="search"),
    url(r'^details/(?P<app_id>.+)$', details, name="details"),
]
