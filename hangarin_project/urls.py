from django.contrib import admin
from django.urls import path
from tasks.views import HomePageView
from tasks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),  # Updated to use class-based view
]
