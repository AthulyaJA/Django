from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def index(request):
    #return HttpResponse("<h1>helloworld</h1>")
    pro1= Student.objects.all
    return render(request,'index.html',{'pro2':pro1})
