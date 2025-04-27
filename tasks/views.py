from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, TaskForm
from .models import Task
from django.utils import timezone
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('tasks:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    # Sort tasks
    sort_by = request.GET.get('sort')
    if sort_by == 'priority':
        tasks = tasks.order_by('-priority', 'due_date')
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date', '-priority')
    
    # Add analytics
    analytics = {
        'total_tasks': tasks.count(),
        'completed_tasks': tasks.filter(status='DONE').count(),
        'overdue_tasks': tasks.filter(due_date__lt=timezone.now()).exclude(status='DONE').count(),
        'high_priority': tasks.filter(priority='H').count(),
    }
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'analytics': analytics,
        'current_sort': sort_by,
        'current_filter': status_filter
    })

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Create New Task',
        'button_text': 'Create'
    })

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Edit Task',
        'button_text': 'Update'
    })

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'DONE'
    task.save()
    messages.success(request, 'Task marked as complete!')
    return redirect('tasks:task_list')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('tasks:task_list')