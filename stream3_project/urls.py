"""stream3_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home_app.urls')),
    url(r'^accounts/', include('accounts_app.urls')),
    url(r'^events/', include('events_app.urls')),
    url(r'^contact/', include('contactform_app.urls')),
    url(r'user/', include('accounts_app.urls')),
    url(r'^packages/', include('packages_app.urls')),

#   ATTEMPT AT SHOWING FAVICON (DIFFICULT IN DJANGO?
#     url(
#             r'^favicon.ico$',
#             RedirectView.as_view(
#                 url=staticfiles_storage.url('favicon.png'),
#                 permanent=False),
#             name="favicon"
#         ),
]
