
from msilib import PID_KEYWORDS
from multiprocessing import context
from django.shortcuts import render
from .models import Blog

# Create your views here.

# performing CRUD operations

# CRUD - Create, Read, Update and Delete

# sending the list to frontend 
def home(request):
    listings = Blog.objects.all()
    context = {
        'list':listings
    }
    return render(request,'home.html',context)

# retriving the list by id

def getlist(request,id):
    getid = Blog.objects.get(id=id)
    context ={
        'getkey':getid
    }
    return render(request,'get.html',context)
