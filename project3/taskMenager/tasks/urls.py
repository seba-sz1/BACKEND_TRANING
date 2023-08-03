from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:taskID>/delete/', views.deleteTask, name='deleteTask'),
    path('tasks/<int:taskID>/', views.detailTask, name='detail'),
    path('create/', views.create_task, name='createTask'), 
]