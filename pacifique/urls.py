from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('articles', views.articles),
    path('article_display', views.article_display),
    path('contact', views.contact),
    
]