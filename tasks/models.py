# tasks/models.py
from django.db import models
from django.utils import timezone
import random

# Base Model
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # This makes the model abstract

# Priority Model
class Priority(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities" # Refactor: Fix plural name

    def __str__(self):
        return self.name

# Category Model
class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" # Refactor: Fix plural name

    def __str__(self):
        return self.name

# Task Model
class Task(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending") # Fixed default capitalization
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

# SubTask Model
class SubTask(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending") # Fixed default capitalization
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks') # Renamed 'parent_task' to 'task' for clarity

    def __str__(self):
        return self.title

# Note Model
class Note(BaseModel):
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notes') # Renamed 'task' from 'task_id' for clarity

    def __str__(self):
        # Truncate content for display if it's long
        return f"Note for {self.task.title}: {self.content[:50]}..." if len(self.content) > 50 else f"Note for {self.task.title}"
