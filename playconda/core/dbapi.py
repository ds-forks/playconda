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
    return [app for app in term.apps.all()]


def get_app(app_id):
    """
    Get an app by App ID
    """
    try:
        return App.objects.get(app_id=app_id)
    except App.DoesNotExist:
        return None

def create_app(**kwargs):
    """
    docstring for create_app
    """
    app = App(**kwargs)
    app.save()
    return app


def get_or_create_apps(app_dicts):
    """
    Get or create a bunch of apps
    """
    apps = []
    for app_dict in app_dicts:
        app_id = app_dict['app_id']
        app = get_app(app_id)
        if app is None:
            app = create_app(**app_dict)
        apps.append(app)
    return apps


def add_app_term(app, term):
    """
    docstring for add_app_term
    """
    app.terms.add(term)
    app.save()
    return app


def add_apps_term(apps, term):
    """
    docstring for add_apps_term
    """
    _apps = []
    for app in apps:
        app = add_app_term(app, term)
        _apps.append(app)
    return _apps
