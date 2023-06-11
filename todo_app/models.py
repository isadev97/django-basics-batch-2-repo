from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    