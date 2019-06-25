from django.db import models
from . import constant


class ParentTask(models.Model):
    task_name = models.CharField(max_length=50)

    class Meta:
        ordering = ('task_name', )

    def __str__(self):
        return self.task_name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.IntegerField()

    class Meta:
        ordering = ('first_name', )

    def __str__(self):
        return self.first_name


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.IntegerField()
    status = models.CharField(choices=constant.PROJECT_STATUS, default='ACTIVE', max_length=15)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ('project_name', )

    def __str__(self):
        return self.project_name



class Task(models.Model):
    task_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.IntegerField()
    status = models.CharField(choices=constant.TASK_STATUS, default='OPEN', max_length=15)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.PROTECT, unique=False)
    parentTask = models.ForeignKey(ParentTask, related_name='parentTask', on_delete=models.PROTECT, unique=False, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, unique=False)

    class Meta:
        ordering = ('task_name', )

    def __str__(self):
        return self.task_name