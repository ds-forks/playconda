#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: dbapi.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-04-30
"""

from playconda.core.models import Term, App


def get_term(text):
    """
    Get term
    """
    try:
        return Term.objects.get(text=text)
    except Term.DoesNotExist:
        return None

def create_term(text):
    """
    Create a term object
    """
    term = Term(text=text)
    term.save()
    return term


def get_apps_for_term(term):
    """
    Get apps for a term
    """
    return [app for app in App.filter(terms__in=term)]
