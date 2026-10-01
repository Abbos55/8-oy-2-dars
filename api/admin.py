from django.contrib import admin

from .models import Course, Student, Genre, Book

admin.site.register([Course, Student, Genre, Book])
