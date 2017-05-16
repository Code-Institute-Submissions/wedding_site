from django.conf.urls import url
from .views import packages, vocalist, harpist, pianist, ceremony, reception

urlpatterns = [
    url(r'^$', packages, name="packages"),
    url(r'^vocalist', vocalist, name="vocalist"),
    url(r'^harpist', harpist, name="harpist"),
    url(r'^pianist', pianist, name="pianist"),
    url(r'^ceremony', ceremony, name="ceremony"),
    url(r'^reception', reception, name="reception"),
]
