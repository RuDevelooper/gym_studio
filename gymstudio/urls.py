"""gymstudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from mainapp.views import *
from scheduleapp.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomePage.as_view(), name='index'),
    re_path(r'^memberships/', Memberships.as_view(), name='membership'),
    re_path(r'^schedule/', Schedule.as_view(), name='schedule'),
    re_path(r'^facilities/', Facilities.as_view(), name='facilities'),
    re_path(r'^team/', Team.as_view(), name='team'),
    re_path(r'^contacts/', Contacts.as_view(), name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
