from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt
from .models import *
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
