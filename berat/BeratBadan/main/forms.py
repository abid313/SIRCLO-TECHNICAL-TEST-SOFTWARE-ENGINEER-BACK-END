from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import ToDoList

class CreateNewList(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['date', 'max', 'min']