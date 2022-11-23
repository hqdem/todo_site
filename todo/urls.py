from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create/', create_task, name='create_task'),
    path('update/<str:pk>/', update_task, name='update_task'),
    path('delete/<str:pk>/', delete_task, name='delete_task'),
    path('change-sorting/', change_sorting, name='change_sorting')
]
