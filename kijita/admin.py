from django.contrib import admin
from . models import Book, Person

# Register your models here.
admin.site.register(Book)
admin.site.register(Person)