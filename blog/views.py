
    
from multiprocessing import context
from django.shortcuts import render, redirect

from blog.forms import BlogForm


from .models import Blog

# Create your views here.

# performing CRUD operations

# CRUD - Create, Read, Update and Delete

# sending the list to frontend 
def home(request):
    return render(request,'home.html')
