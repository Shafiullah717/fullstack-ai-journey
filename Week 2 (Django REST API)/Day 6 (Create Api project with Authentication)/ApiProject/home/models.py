from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)