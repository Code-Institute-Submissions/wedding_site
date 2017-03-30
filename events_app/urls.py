from django.conf.urls import url
import views

urlpatterns = [
    # url(r'^(?P<id>\d+)/$', views.event, name='event'),
    url(r'^wedding$', views.userevent, name='user_event'),
]
