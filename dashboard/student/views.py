from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
# Create your views here.

def studentlist(request):
    students = User.objects.filter(is_active = True).exclude(is_superuser = True)
    
    context = {'output':students}

    return render(request,"home.html",context)


def acedamicviews(request,id):
     try:
        details = AcademicDetails.objects.filter(authur=id)
     except AcademicDetails.DoesNotExist:
        raise Http404("Question does not exist")
     return render(request,'acedamicdetails.html',{'details':details})
    
def workviews(request,id):
     try:
        details = WorkProcess.objects.filter(authur=id)
        #comments = details.comments.all()
     except WorkProcess.DoesNotExist:
        raise Http404("Question does not exist")
     return render(request,'workdetails.html',{'details':details})
