from numbers import Integral
from django.db import models

# Create your models here.
class ToDoList(models.Model):
    date = models.DateField()
    max = models.IntegerField()
    min = models.IntegerField()
    diff = models.IntegerField()
    
    def __str__(self):
        return self.date, self.max, self.min
