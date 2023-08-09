from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('articles/', views.ListCreateArticle.as_view()),
    path('articles/<int:pk>/', views.DetailDeleteArticle.as_view()),
    path('users/', views.ListCreateUsers.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)