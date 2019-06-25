from django.contrib import admin
from .models import Project, Task, User, ParentTask

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)
admin.site.register(ParentTask)