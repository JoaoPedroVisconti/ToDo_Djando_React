from django.db import models
from django.db.models.base import Model

# Create your models here


class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title
