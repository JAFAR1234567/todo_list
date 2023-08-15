from django.urls import path
from . import views
urlpatterns = [
    path('', views.TodoFormView.as_view(), name='add_todo'),
    path('show_todo/', views.TodoListView.as_view(), name='show_todo'),
    path('edit_todo/<int:pk>', views.TodoUpdateView.as_view(), name='edit_todo'),
    path('delete_todo/<int:pk>', views.TodoDeletView.as_view(), name='delete_todo'),
    path('complete_todo/', views.TodoCompleteView.as_view(), name='complete_todo'),
]