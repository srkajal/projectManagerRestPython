from django.urls import path
from . import views


urlpatterns = [
    path('projects', views.ProjectList.as_view()),
    path('projects/active', views.ProjectActiveList.as_view()),
    path('project/<int:pk>', views.ProjectDetails.as_view()),
    path('project/create', views.ProjectCreate.as_view()),
    path('project/update/<int:pk>', views.ProjectUpdate.as_view()),

    path('parents', views.ParentTaskList.as_view()),
    path('parent/<int:pk>', views.ParentTaskDetails.as_view()),
    path('parent/create', views.ParentCreate.as_view()),
    path('parent/update/<int:pk>', views.ParentUpdate.as_view()),

    path('tasks', views.TaskList.as_view()),
    path('task/<int:pk>', views.TaskDetails.as_view()),
    path('task/create', views.TaskCreate.as_view()),
    path('task/update/<int:pk>', views.TaskUpdate.as_view()),

    path('users', views.UserList.as_view()),
    path('users/noProject', views.UserNoProjectList.as_view()),
    path('user/<int:pk>', views.UserDetails.as_view()),
    path('user/create', views.UserCreate.as_view()),
    path('user/update/<int:pk>', views.UserUpdate.as_view()),
]