"""projeto_aula2 URL Configuration

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

from app1.views import list_authors, detail_authors, delete_authors, list_book, detail_book, list_pub

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/list/', list_authors),
    path('author/detail/<int:pk>/', detail_authors),
    path('author/delete/<int:pk>/', delete_authors),
    path('book/list/', list_book),
    path('book/detail/<int:pk>/', detail_book),
    path('pub/list/', list_pub)
]
