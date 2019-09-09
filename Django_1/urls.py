"""Django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import re

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from Django_1 import settings
from app1 import views, login
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('admin/', admin.site.urls),
    path('hello/',views.hellword),
    # path('sending/', views.user_info),
    # path('getinfo/', views.user_history),
    # path('app1/',admin.site.urls),
    # path('user/', views.user_info, name='index'),
    # url('login-form/',views.app),
    # path('login/',views.geturl),
    # url('login/', views.user_info),
    url('login/', views.login),
    url('loginapi/',login.login),
    url('regist/',views.regist),
    url('registapi/',login.regist),
    url('ywweb',views.ywweb)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)


