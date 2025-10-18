from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Category, Note, Priority, SubTask, Task
from tasks.forms import CategoryForm, NoteForm, PriorityForm, SubTaskForm, TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import timezone

class HomePageView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["total_tasks"] = Task.objects.count()
        context["total_subtasks"] = SubTask.objects.count()
        context["total_notes"] = Note.objects.count()
        context["total_categories"] = Category.objects.count()
        context["total_priorities"] = Priority.objects.count()

        context["completed_tasks"] = Task.objects.filter(status="Completed").count()
        context["pending_subtasks"] = SubTask.objects.filter(status="Pending").count()

        return context

# ListViews here
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs

    def get_ordering(self):
        allowed = ["name", "-name", "created_at", "-created_at"]
        sort_by = self.request.GET.get("sort_by")
        return sort_by if sort_by in allowed else "name"


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(task__title__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = ["created_at", "-created_at", "task__title", "-task__title"]
        sort_by = self.request.GET.get("sort_by")
        return sort_by if sort_by in allowed else "-created_at"


class PriorityListView(LoginRequiredMixin, ListView):
    model = Priority
    context_object_name = 'priorities'
    template_name = 'priority_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs

    def get_ordering(self):
        allowed = ["name", "-name", "created_at", "-created_at"]
        sort_by = self.request.GET.get("sort_by")
        return sort_by if sort_by in allowed else "name"


class SubTaskListView(LoginRequiredMixin, ListView):
    model = SubTask
    context_object_name = 'subtasks'
    template_name = 'subtask_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(status__icontains=query) |
                Q(task__title__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = [
            "title", "-title",
            "status", "-status",
            "created_at", "-created_at",
            "task__title", "-task__title"
        ]
        sort_by = self.request.GET.get("sort_by")
        return sort_by if sort_by in allowed else "title"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(status__icontains=query) |
                Q(priority__name__icontains=query) |
                Q(category__name__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = [
            "title", "-title",
            "status", "-status",
            "created_at", "-created_at",
            "priority__name", "-priority__name",
            "category__name", "-category__name"
        ]
        sort_by = self.request.GET.get("sort_by")
        return sort_by if sort_by in allowed else "title"
    
# CreateViews here
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

# UpdateViews here
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')
    
class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')
    
class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

# DeleteViews here
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')