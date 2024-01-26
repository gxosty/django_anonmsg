"""
URL configuration for anonmsg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('create_message', views.create_message, name="create_message"),
    path('read_message', views.read_message, name="read_message"),
    path('message_info', views.message_info, name="message_info"),
    path('show_message', views.show_message, name="show_message"),

    path('anonmsgadminpage/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
]
