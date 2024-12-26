"""
URL configuration for module_19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from task1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', main_page),
    path('shop/', shop),
    path('basket/', basket),
    path('base_menu/', base_menu),
    path('', form_register),
    path('bd_buyer/', bd_buyer),
    # path('authorizations/', authorization_user),
    path('platform/news/', news),
]
