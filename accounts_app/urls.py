from django.conf.urls import url
from .views import register, login, logout, success
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

urlpatterns = [
    url(r'^register/$', register, name='register'),
    # url(r'^profile$', profile, name='profile'),
    url(r'^success/$', success, name='success'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
