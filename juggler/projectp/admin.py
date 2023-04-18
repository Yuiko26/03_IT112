from django.contrib import admin
from projectp.models import Project, Task
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    