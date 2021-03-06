from django.db import models

# Create your models here.
class  Student(models.Model):
    name=models.CharField(max_length=255)
    RollNo=models.IntegerField()
    Mark=models.FloatField()
    Depart=models.CharField(max_length=255)
    image=models.CharField(max_length=255)

class  Stud(models.Model):
    name=models.CharField(max_length=255)
    RollNo=models.IntegerField()
    Mark=models.FloatField()
    Depart=models.CharField(max_length=255)
    image=models.CharField(max_length=255)