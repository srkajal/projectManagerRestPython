from rest_framework import generics
from .serializers import ProjectSerializer, TaskSerializer, ParentTaskSerializer, UserSerializer
from .models import Project, Task, ParentTask, User


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectActiveList(generics.ListAPIView):
    queryset = Project.objects.filter(status='ACTIVE')
    serializer_class = ProjectSerializer

class ProjectDetails(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdate(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetails(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ParentTaskList(generics.ListAPIView):
    queryset = ParentTask.objects.all()
    serializer_class = ParentTaskSerializer


class ParentTaskDetails(generics.RetrieveAPIView):
    queryset = ParentTask.objects.all()
    serializer_class = ParentTaskSerializer


class ParentCreate(generics.CreateAPIView):
    queryset = ParentTask.objects.all()
    serializer_class = ParentTaskSerializer


class ParentUpdate(generics.UpdateAPIView):
    queryset = ParentTask.objects.all()
    serializer_class = ParentTaskSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserNoProjectList(generics.ListAPIView):
    queryset = User.objects.exclude(project__user__isnull=False)
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer