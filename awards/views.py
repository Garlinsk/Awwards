from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect,  HttpResponseRedirect
from django.templatetags.static import static
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer


# Create your views here.

def index(request):
    date = dt.date.today()
    projects = Projects.get_projects()

    return render(request, 'index.html', {"date": date, "projects": projects})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
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


class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Projects.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
