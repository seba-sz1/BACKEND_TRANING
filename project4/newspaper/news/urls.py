from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('articles/', views.list_create_articles),
    path('articles/<int:articleID>/', views.article_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)