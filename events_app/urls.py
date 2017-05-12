from django.conf.urls import url
import views

urlpatterns = [
    url(r'^wedding$', views.userevent, name='user_event'),
    url(r'^charge$', views.charge, name='charge'),
]
