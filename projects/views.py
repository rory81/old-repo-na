from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm
from datetime import datetime
# Create your views here.


def get_projects(request):
    projects = Project.objects.filter(created_date__lte=datetime.now()).order_by('-created_date')

    return render(request, 'projects/projects_lists.html', {'projects': projects})


def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_projects')
    form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('get_projects')
    form = ProjectForm(instance=project)
    return render(request, 'projects/edit_project.html', {'form': form})


def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('get_projects')
