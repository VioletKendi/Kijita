from pydoc import synopsis
from turtle import mode
from django.db import models

# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length= 64)
    Email = models.EmailField(primary_key= True)
    Password = models.CharField(max_length= 20)

class Book(models.Model):
    Title = models.CharField(max_length = 64)
    Author = models.CharField(max_length= 64)
    Synopsis = models.CharField(max_length= 300)
    Uploaded_by = models.ForeignKey(Person, on_delete= models.CASCADE, related_name= "Uploadedby")
    Category = models.Choices("Educational", "Novels")



