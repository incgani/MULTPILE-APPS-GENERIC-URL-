"""project_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from App1.views import *
from App2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_view_App_01/',first_view_App_01,name='first_view_App_01'),
    path('Second_view_App_01/',Second_view_App_01,name='Second_view_App_01'),
    path('first_view_App_02/',first_view_App_02,name='first_view_App_02'),
    path('Second_view_App_02/',Second_view_App_02,name='Second_view_App_02'),
]
