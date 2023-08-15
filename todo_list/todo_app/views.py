from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from todo_app.forms import TodoForm
from todo_app.models import TaskModel
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

class TodoFormView(CreateView):
    model = TaskModel
    template_name = 'create_todo.html'
    form_class = TodoForm
    success_url = reverse_lazy('show_todo')

class TodoListView(ListView):
    model = TaskModel
    template_name = 'show_todo.html'
    context_object_name = 'todolist'  
    
class TodoUpdateView(UpdateView):
    model = TaskModel
    template_name = 'create_todo.html'
    form_class = TodoForm
    success_url = reverse_lazy('show_todo')  

    
class TodoDeletView(DeleteView):
    model = TaskModel
    template_name = 'delete.html'
    success_url = reverse_lazy('show_todo')    
    
class TodoCompleteView(ListView):
    model = TaskModel
    template_name = 'complete_todo.html'
    context_object_name = 'todolist'     