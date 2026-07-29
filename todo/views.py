from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignupForm, TodoForm
from .models import Todo


@login_required
def todo_list(request):
    todos = Todo.objects.filter(owner=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(
        request,
        'todo/todo_list.html',
        {'todos': todos, 'form': form},
    )


@login_required
def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, owner=request.user)

    if request.method == 'POST':
        todo.completed = True
        todo.save()

    return redirect('todo_list')


@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, owner=request.user)

    if request.method == 'POST':
        todo.delete()

    return redirect('todo_list')


@login_required
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, owner=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/todo_edit.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = SignupForm()

    return render(request, 'todo/signup.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)

    return redirect('login')
