#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: extractor.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-04-30
"""
import requests
from pyquery import PyQuery as pq

from django.conf import settings

def app_dict_for_card(card):
    """
    Get app details for the card
    """
    href = card(".cover .card-click-target")[0].attrib.get('href')
    icon_url = card(".cover-image")[0].attrib.get("data-cover-large")
    developer_name = card(".subtitle-container .subtitle")[0].text
    app_name = card(".title")[0].text
    app_id = href.split("=")[1]
    resp = requests.get(settings.PLAY_DOMAIN + href)
    doc2 = pq(resp.content)
    try:
        developer_email = doc2(".dev-link")[1].attrib.get('href').split(":")[1]
    except IndexError:
        developer_email = doc2(".dev-link")[0].attrib.get('href').split(":")[1]
    return dict(
        app_id=app_id, app_name=app_name, developer_name=developer_name,
        developer_email=developer_email, icon_url=icon_url)

def app_dicts_for_text(text):
    """
    Get the App dicts for the given text
    """
    url = settings.SEARCH_URL % text
    resp = requests.get(url)
    doc = pq(resp.content)
    app_dicts = []
    for el in doc(".card")[:10]:
        card = pq(el)
        app_dict = app_dict_for_card(card)
        app_dicts.append(app_dict)
    return app_dicts
