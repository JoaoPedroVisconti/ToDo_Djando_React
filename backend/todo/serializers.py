from django.db.models import fields
from rest_framework import serializers

from .models import Todo

# Convert the model instances to JSON for the frontend access

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed')