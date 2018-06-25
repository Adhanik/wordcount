"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views#. symbolises current directory.

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),#home redirects to views template home function which in turn returns a home.html page
    path('youth/',views.youth),
    path('countword/',views.count,name='count'),#NAME IS directly related to form action.
    path('about/',views.about,name='about'),
]
