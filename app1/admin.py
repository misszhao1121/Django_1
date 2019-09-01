from django.contrib import admin

# Register your models here.
from django.http import request
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
# Create your views here.
def hellword(request):
    print(request.methon)
    return HttpResponse('你好')