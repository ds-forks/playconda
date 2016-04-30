from django.shortcuts import render, redirect


from playconda.core.dbapi import get_term, create_term, get_app, \
    get_or_create_apps, add_apps_term
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
    text = request.GET.get("text").strip()
    if text == "":
        return redirect("index")
    term = get_term(text)
    if term is None:
        term = create_term(text)
        app_dicts = app_dicts_for_text(text)
        apps = get_or_create_apps(app_dicts)
        add_apps_term(apps, term)
    context = dict(term=term)
    return render(request, "search.html", context)


def details(request, app_id):
    """
    View details of an app
    """
    text = request.GET.get("text").strip()
    app = get_app(app_id)
    print(text)
    if text == "" or app is None:
        return redirect("index")
    context = dict(text=text, app=app)
    return render(request, "details.html", context)
