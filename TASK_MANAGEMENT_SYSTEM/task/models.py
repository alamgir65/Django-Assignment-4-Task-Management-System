from django.db import models
from category.models import CategoryModel
import datetime
# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_Completed = models.BooleanField(default=False)
    taskAssignedDate = models.DateField(default=datetime.datetime.now())
    categories = models.ManyToManyField(CategoryModel)
    
    def __str__(self):
        return self.taskTitle
