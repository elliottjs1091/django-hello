from django.shortcuts import render
from django.http import HttpResponse

def index(request):
# Create your views here.
    return HttpResponse('Hello World!')
