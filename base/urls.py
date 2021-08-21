from django.urls import path

from .views import CustomLoginView, RegisterPage, TaskCreate, TaskList, TastDetail, TaskUpdate, TaskDelete, TaskReorder
from django.contrib.auth.views import LogoutView

app_name = 'base'

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TastDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='create_task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

    # AUTH
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register')
]