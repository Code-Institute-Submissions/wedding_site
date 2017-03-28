from django.conf.urls import url
import views

urlpatterns = [
    url(r'event', views.event, name='event'),
]
