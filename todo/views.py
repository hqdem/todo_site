from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm


def index(request):
    user = request.user
    if user.is_anonymous:
        return render(request, 'todo/index.html', context={'form': TaskForm()})

    sorting = request.session.get('sorting', 'created_at')
    tasks = Task.objects.filter(author=user).order_by(sorting)
    form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/index.html', context=context)


@login_required
def update_task(request, pk):
    user = request.user
    task = get_object_or_404(Task, pk=pk, author=user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = TaskForm(instance=task)

    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'todo/update.html', context=context)


@login_required
@require_POST
def create_task(request):
    user = request.user

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.author = user
            inst.save()
            return redirect('home')
        else:
            print(form.errors)
    return redirect('home')


@login_required
def delete_task(request, pk):
    user = request.user
    task = get_object_or_404(Task, pk=pk, author=user)

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {
        'task': task,
    }
    return render(request, 'todo/delete.html', context=context)


def change_sorting(request):
    now_sorting = request.session.get('sorting', None)
    if now_sorting is None or now_sorting == 'created_at':
        request.session['sorting'] = '-created_at'
        return redirect('home')
    if now_sorting == '-created_at':
        request.session['sorting'] = 'created_at'
        return redirect('home')
        