from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('playconda.core.urls'))
]
