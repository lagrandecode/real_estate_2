
    
from multiprocessing import context
from django.shortcuts import render, redirect

from blog.forms import BlogForm


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

# end of retrieving id 

# code for updating the list 

def updatelist(request,id):
    update = Blog.objects.get(id=id)
    updateform = BlogForm(instance=update)
    if request.method == 'POST':
        updateform = BlogForm(request.POST, instance=update)
        if updateform.is_valid():
            updateform.save()
        return render(request,'update.html',context)

def deletelist(request,id):
    deleteitem = Blog.objects.get(id=id)
    d
    return redirect('/')