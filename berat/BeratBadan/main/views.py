from operator import is_
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>Welcome %s!</h1>" %ls.date)

def home(response):
    return render(response, "main/home.html")

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            date = form.cleaned_data["date"].strftime("%Y-%m-%d")
            max = form.cleaned_data["max"]
            min = form.cleaned_data["min"]
            diff = max - min
            t = ToDoList(date=date, max=max, min=min, diff=diff)
            t.save()
        
        return HttpResponseRedirect("/%s" %t.id)
            
    else:
        form = CreateNewList()
        
    return render(response, "main/create.html", {"form":form})

def update(response, id):
    if response.method == "POST":
        ls = ToDoList.objects.get(id=id)
        form = ToDoList(request.POST, instance=ls)
        if form.is_valid():
            form.save()
    
    else:
        ls = ToDoList.objects.get(id=id)
        form = ToDoList(instance=ls)
    
    return render(response, "main/update.html", {"form":form})

def delete(response, id):
    if response.method == "POST":
        ls = ToDoList.objects.get(id=id)
        ls.delete()
        return HttpResponseRedirect("/")