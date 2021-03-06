from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="dash"),
    path('product/',views.product,name="product"),
    path('view/<str:PK>/',views.view,name="customer")


]