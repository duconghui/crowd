"""crowdfunding URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from crowdfund import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^myself/', views.myself, name='myself'),
    url(r'^thefirst/', views.thefirst, name='thefirst'),
    url(r'^add/', views.add, name='add'),
    url(r'^investment/', views.investment, name='investment'),
    url(r'^investor/', views.investor, name='investor'),
    url(r'^choose', views.choose, name='choose'),
    url(r'^projects', views.projects, name='projects'),
    url(r'^project_details', views.project_details, name='project_details'),
    url(r'^guide', views.guide, name='guide'),
    url(r'^filter', views.filter, name='filter'),
    url(r'^xiaoxi', views.filter, name='xiaoxi'),
    url(r'^help', views.guide, name='help'),
    url(r'^project_details2', views.project_details2, name='project_details2'),
]

app_name = 'crowdfund'
