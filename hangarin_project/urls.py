from django.contrib import admin
from django.urls import path, include
from tasks.views import (
    HomePageView,
    CategoryListView, NoteListView, PriorityListView, SubTaskListView, TaskListView,
    CategoryCreateView, NoteCreateView, PriorityCreateView, SubTaskCreateView, TaskCreateView,
    CategoryUpdateView, NoteUpdateView, PriorityUpdateView, SubTaskUpdateView, TaskUpdateView,
    CategoryDeleteView, NoteDeleteView, PriorityDeleteView, SubTaskDeleteView, TaskDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomePageView.as_view(), name='home'),

    # ListView
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('note/', NoteListView.as_view(), name='note-list'),
    path('priority/', PriorityListView.as_view(), name='priority-list'),
    path('subtask/', SubTaskListView.as_view(), name='subtask-list'),
    path('task/', TaskListView.as_view(), name='task-list'),

    # CreateView
    path('category/add/', CategoryCreateView.as_view(), name='category-add'),
    path('note/add/', NoteCreateView.as_view(), name='note-add'),
    path('priority/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('subtask/add/', SubTaskCreateView.as_view(), name='subtask-add'),
    path('task/add/', TaskCreateView.as_view(), name='task-add'),

    # UpdateView
    path('category/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('note/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('priority/<int:pk>/', PriorityUpdateView.as_view(), name='priority-update'),
    path('subtask/<int:pk>/', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('task/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),

    # DeleteView
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('priority/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),
    path('subtask/<int:pk>/delete/', SubTaskDeleteView.as_view(), name='subtask-delete'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]