from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def reportedissue(request):
    return render(request,'reportedissue.html')

def reportissue(request):
    return render(request,'reportissue.html')

def reportedissuesub(request):
    return render(request,'reportedissuesub.html')

