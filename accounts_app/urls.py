from django.conf.urls import url
from .views import register, profile, login, logout, success

urlpatterns = [
    url(r'^register$', register, name='register'),
    url(r'^profile$', profile, name='profile'),
    url(r'^success$', success, name='success'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
]
