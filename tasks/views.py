from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from django.urls import reverse

def home(request):
    """
    Display all tasks and handle quick task creation.
    """
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:home')
    return render(request, 'home.html', {'tasks': tasks, 'form': form})

def create_task(request):
    """
    Create a new task via a dedicated page.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:home')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def toggle_task(request, pk):
    """
    Toggle the completion status of a task.
    """
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:home')

def delete_task(request, pk):
    """
    Delete a task after confirmation.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:home')
    return render(request, 'delete_task.html', {'task': task})

def edit_task(request, pk):
    """
    Edit an existing task.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def about(request):
    """
    Render the about page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    Render the contact page.
    """
    return render(request, 'contact.html')

def register(request):
    """
    Register a new user and log them in.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    """
    Log in an existing user.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tasks:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
    Log out the current user.
    """
    logout(request)
    return redirect('tasks:home')
