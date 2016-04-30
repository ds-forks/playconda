from django.shortcuts import render


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
    app_dicts = app_dicts_for_text(text)
    print(app_dicts)
    context = dict(text=text)
    return render(request, "search.html", context)


def details(request, app_id):
    """
    View details of an app
    """
    return render(request, "details.html")
