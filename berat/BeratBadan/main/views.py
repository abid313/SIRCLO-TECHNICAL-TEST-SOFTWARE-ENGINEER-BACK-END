from audioop import avg
from curses import tparm
from operator import is_
from statistics import mean
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList
from django.db.models import Avg, Max, Min, Sum


# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/index.html", {'ls':ls})

def home(response):
    datas = ToDoList.objects.all()
    maksAvg = datas.aggregate(Avg('max'))
    minAvg = datas.aggregate(Avg('min'))
    diffAvg = datas.aggregate(Avg('diff'))
    context = {'datas': datas, 'max' : maksAvg['max__avg'], 'min' : minAvg['min__avg'], 'diff' : diffAvg['diff__avg']}
    return render(response, "main/home.html", context)

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
        
        return HttpResponseRedirect("/"+str(t.id))
            
    else:
        form = CreateNewList()
        
    return render(response, "main/create.html", {"form":form})

def update(response, id):
    data = ToDoList.objects.get(id=id)
    data.diff = data.max - data.min
    form = CreateNewList(instance=data)
    if response.method == "POST":
        form = CreateNewList(response.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+str(data.id))
    
    context = {'form': form, 'item': data}
    return render(response, "main/update.html", context)

def delete(response, id):
    if response.method == "POST":
        ls = ToDoList.objects.get(id=id)
        ls.delete()
        return HttpResponseRedirect("/")