from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(
        request,
        'todo/todo_list.html',
        {'todos': todos, 'form': form},
    )


def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == 'POST':
        todo.completed = True
        todo.save()

    return redirect('todo_list')
