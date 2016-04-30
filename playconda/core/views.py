from django.shortcuts import render


from playconda.core.dbapi import get_term, create_term, \
    get_or_create_apps, add_apps_term, get_apps_for_term
from playconda.core.extractor import app_dicts_for_text


def index(request):
    """
    docstring for index
    """
    return render(request, "index.html")


def search(request):
    """
    Search for a text
    """
    text = request.GET.get("text")
    term = get_term(text)
    if term is None:
        term = create_term(text)
        app_dicts = app_dicts_for_text(text)
        apps = get_or_create_apps(app_dicts)
        apps = add_apps_term(apps, term)
    else:
        apps = get_apps_for_term(term)
    context = dict(text=text, term=term, apps=apps)
    return render(request, "search.html", context)


def details(request, app_id):
    """
    View details of an app
    """
    return render(request, "details.html")
