from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    date_create=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200,choices=CATEGORY)
    category=models.CharField(max_length=200)
    dis=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    status=(
        ('Pending','Pending'),
        ('Out of delivery','Out of delivery'),
        ('Deliverd','Deliverd')
        
    )
    customer=models.ForeignKey(Customer,null=True ,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product, null=True,on_delete=models.SET_NULL)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=200,choices=status)

    def __str__(self):
        return self.product.name