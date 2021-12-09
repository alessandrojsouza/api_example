from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=40)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
