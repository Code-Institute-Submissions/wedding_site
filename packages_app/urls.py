from django.conf.urls import url
from .views import packages, ceremony, reception

urlpatterns = [
    url(r'^$', packages, name="packages"),
    url(r'^ceremony', ceremony, name="ceremony"),
    url(r'^reception', reception, name="reception"),
]
