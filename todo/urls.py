from django.urls import path

from . import views


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:todo_id>/complete/', views.complete_todo, name='complete_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
]
