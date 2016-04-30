from django.shortcuts import render


def index(request):
    """
    docstring for index
    """
    return render(request, "index.html")


def search(request):
    """
    Search for a text
    """
    return render(request, "search.html")


def detail(request, app_id):
    """
    View details of an app
    """
    return render(request, "detail.html")
