from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def index(request):
    pro1= Customer.objects.all
    pro2=Product.objects.all
    pro3=Order.objects.all
    total_order=Order.objects.count
    deliverd=Order.objects.filter(status='Deliverd').count()
    Pending=Order.objects.filter(status='Pending').count()
    context={'customer':pro1,'order':pro3,'total_order':total_order,'product':pro2,'deliverd':deliverd,'Pending':Pending}
    #return HttpResponse("<h1>helloworld</h1>")
    return render(request,'accounts/dashboard.html',context)
def product(request):
    product=Product.objects.all()
    return render(request,'accounts/product.html',{'product':product})

def view(request,PK):
    customer=Customer.objects.get(id=PK)
    return render(request,'accounts/view.html',{'customer':customer})
