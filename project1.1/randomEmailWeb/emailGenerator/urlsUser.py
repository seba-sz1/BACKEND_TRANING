from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('exitEmail/', views.exitEmail, name="exitEmail"),
    path('about/', views.about, name="about"),
]

#TODO --> finish and rebuid project
