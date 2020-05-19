from django.urls import path
from . import views

urlpatterns = [
    path('', views.users.index, name='index'),
    path('create_users/', views.users.create_users, name='create_users'),
    path('list_users/', views.users.list_users, name='list_users'),
    path('create_perms/', views.users.create_perms, name='create_perms'),
]
