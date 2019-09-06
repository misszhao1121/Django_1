from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, UserIPInfo, BrowseInfo
# Register your models here.
from django.http import request
from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(BrowseInfo)
