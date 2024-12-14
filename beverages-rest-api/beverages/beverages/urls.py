"""
URL configuration for beverages project.

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
from rest_framework.urlpatterns import format_suffix_patterns

from beverages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beverages/', views.beverage_list),  # http://127.0.0.1:8000/beverages/
    path('beverages/<int:id>', views.beverage_detail),  # http://127.0.0.1:8000/beverages/2/
]

urlpatterns = format_suffix_patterns(urlpatterns)
