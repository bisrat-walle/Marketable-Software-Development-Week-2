from django.contrib import admin
from django.urls import path
from todo import views as todo_views

urlpatterns = [
    path('', todo_views.index, name='tasks'),
    path('admin/', admin.site.urls),
]
