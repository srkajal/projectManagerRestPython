from rest_framework import serializers
from .models import Project, Task, ParentTask, User
from . import constant

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    total_task_count = serializers.SerializerMethodField()
    completed_task_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'start_date', 'end_date', 'priority', 'status', 'user', 'total_task_count', 'completed_task_count')

    def get_total_task_count(self, obj):
        return Task.objects.filter(project_id=obj.id).count()
    
    def get_completed_task_count(self, obj):
        return Task.objects.filter(project_id=obj.id).filter(status=constant.CLOSED).count()


class TaskSerializer(serializers.ModelSerializer):
    parentTask = serializers.StringRelatedField(many=False)
    project = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Task
        fields = ('id', 'task_name', 'start_date', 'end_date', 'priority', 'status', 'project', 'parentTask', 'user',)


class ParentTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentTask
        fields = ('id', 'task_name',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'employee_id',)