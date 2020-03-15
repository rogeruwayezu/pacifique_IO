# from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # url(r'^post/new', views.new_post, name='post_image'),

    path('', views.home, name='home'),

    path('articles', views.articles, name='articles'),
    path('article_display/<int:article_id>/', views.article_display, name='article_display'),
    path('new_article', views.new_article, name='new_article'),

    path('contact', views.contact, name='contact'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)