from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
import datetime as dt
from .models import *
from .forms import *
# Create your views here.


def index(request):
    date = dt.date.today()
    projects = Projects.get_projects()

    return render(request, 'index.html', {"date": date, "projects": projects})


def search_projects(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Projects.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})




def get_project(request, id):

    try:
        project = Projects.objects.get(pk=id)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, "projects.html", {"project": project})


# @login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Author = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new-project.html', {"form": form})


# @login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    Author = current_user
    projects = Projects.get_by_author(Author)

    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')

    else:
        form = ProfileUpdateForm()

    return render(request, 'registration/profile.html', {"form": form, "projects": projects})


