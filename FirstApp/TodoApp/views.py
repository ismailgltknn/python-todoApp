from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todos
from .forms import ListForm
from django.contrib import messages

name = "İsmail GÜLTEKİN"
def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todoList = Todos.objects.all()
            messages.success(request, "İşlem başarılı.")
            return redirect('/')
    else:
        todoList = Todos.objects.all()
        return render(request, "TodoApp/index.html",  {"creator":name, "todoList":todoList})

def about(request):
    return render(request, "TodoApp/about.html",  {"creator":name})

def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todoList = Todos.objects.all()
            messages.success(request, "İşlem başarılı.")
            return redirect("index")
    else:
        todoList = Todos.objects.all()
        return render(request, "TodoApp/create.html",  {"creator":name, "todoList":todoList})
    
def delete(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    todo.delete()
    return redirect("index")

def yes_finish(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    todo.finished = False
    todo.save()
    return redirect("index")

def no_finish(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    todo.finished = True
    todo.save()
    return redirect("index")

def update(request, todo_id):
    if request.method == "POST":
        todoList = Todos.objects.get(pk=todo_id)
        form = ListForm(request.POST or None, instance=todoList)
        if form.is_valid:
            form.save()
            messages.success(request, "İşlem başarılı.")
            return redirect("index")
    else:
        todoList = Todos.objects.all()
        return render(request, "TodoApp/update.html",  {"creator":name, "todoList":todoList})