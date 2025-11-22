"""familytree URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('ezzadmin/', admin.site.urls),
    #path('familytree/', include('familytree.urls')),
    path('familytree/', include('django.contrib.auth.urls')),
    path('tree_fa/', TemplateView.as_view(template_name='familytree.html'), name='tree_fa'),
    path('tree_en/', TemplateView.as_view(template_name='familytreeen.html'), name='tree_en'),
    path('tree_exp/', TemplateView.as_view(template_name='familytreeexp.html'), name='tree_exp'),
    path('help_fa/', TemplateView.as_view(template_name='help.html'), name='help_fa'),
    path('help_en/', TemplateView.as_view(template_name='help_en.html'), name='help_en'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

