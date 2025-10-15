from django.contrib import admin
from .models import Task, SubTask, Category, Priority, Note

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',) 

class SubTaskInline(admin.TabularInline): 
    model = SubTask
    extra = 1

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority', 'category')
    list_filter = ('status', 'priority', 'category') 
    search_fields = ('title', 'description') 

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'get_parent_task_name') 
    list_filter = ('status',) 
    search_fields = ('title',)

    def get_parent_task_name(self, obj):
        return obj.task.title 
    get_parent_task_name.short_description = 'Parent Task Name' 

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task', 'content', 'created_at') 
    list_filter = ('created_at',) 
    search_fields = ('content',) 
