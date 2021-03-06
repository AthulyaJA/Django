from django.shortcuts import render
from django.http import HttpResponse
from  . models import Products


# Create your views here
def index(request):
    #return HttpResponse("<h1>Hello world</h")
    pro1= Products.objects.all
    return render(request,'index.html',{'pro2':pro1})