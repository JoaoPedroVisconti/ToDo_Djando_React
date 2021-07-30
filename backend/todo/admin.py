from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'completed')

# Change the way things display on admin page


admin.site.register(Todo, TodoAdmin)
