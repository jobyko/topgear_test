from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("GCP pipeline test - set image | image create and deploy ")
    
