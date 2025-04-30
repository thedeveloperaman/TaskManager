from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin interface for Task model."""
    list_display = ('title', 'category', 'completed')
    list_filter = ('category', 'completed')
    search_fields = ('title',)
