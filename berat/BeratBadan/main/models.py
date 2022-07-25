from django.db import models

# Create your models here.
class ToDoList(models.Model):
    date = models.DateField()
    max = models.IntegerField()
    min = models.IntegerField()
    diff = models.IntegerField()
    
    def __str__(self):
        return self.date, self.max, self.min, self.diff
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    date = models.DateField()
    max = models.IntegerField()
    min = models.IntegerField()
    diff = models.IntegerField()
    
    def __str__(self):
        return self.date, self.max, self.min, self.diff