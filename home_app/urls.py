from django.conf.urls import url
from .views import home, about, listen, faq, blog

urlpatterns = [
    url(r'^$', home, name="index"),
    url(r'^about$', about, name="about"),
    url(r'^listen', listen, name="listen"),
    url(r'^faq', faq, name="faq"),
    url(r'^blog', blog, name="blog"),
]


