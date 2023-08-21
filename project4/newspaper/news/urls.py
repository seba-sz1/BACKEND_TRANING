from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('articles/', views.ListCreateArticle.as_view(), name='articles'),
    path('articles/<int:pk>/', views.DetailDeleteArticle.as_view(), name='articleDetail'),
    path('users/', views.ListCreateUsers.as_view(), name= 'users'),
    path('get-token/', obtain_auth_token, name= 'get_token'),
    path('', views.APIRoot.as_view(), name= 'home')
]

urlpatterns = format_suffix_patterns(urlpatterns)
