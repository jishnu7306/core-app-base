from django.http import request
from django.shortcuts import render

# Create your views here.
#jishnu
def index(request):
    return render(request,'index.html')
def reportedissue(request):
    return render(request,'reportedissue.html')
def reportissue(request):
    return render(request,'reportissue.html')
def reportedissuesub(request):
    return render(request,'reportedissuesub.html')
def applyleave(request):
    return render(request,'applyleave.html')
def applyleavesub(request):
    return render(request,'applyleavesub.html')

#saneesha
def reportissuetrainers(request):
    return render(request,'reportissuetrainers.html')
def reportissuetrainees(request):
    return render(request,'reportissuetrainees.html')
def trainerunsolvedissue(request):
    return render(request,'trainerunsolvedissue.html')
def trainersolvedissue(request):
    return render(request,'trainersolvedissue.html')
def traineessolved(request):
    return render(request,'traineessolved.html')
def traineesunsolved(request):
    return render(request,'traineesunsolved.html')



#sebin
def Requestedleave(request):
    return render(request, 'Requestedleave.html')

#althaf
def trainers_leave(request):
    return render(request, 'trainers_leave.html')
def trainees_leave(request):
    return render(request, 'trainees_leave.html')

