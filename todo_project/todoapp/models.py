from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):

    todo = models.CharField(max_length=200,null=True)
    completed = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo
    
    def get_absolute_url(self):
        return reverse('home')
    