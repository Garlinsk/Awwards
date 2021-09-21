from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.


def index(request):
    return render (request,'index.html')
