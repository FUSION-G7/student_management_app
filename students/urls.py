from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.student_list, name='student_list'),

    path(
        'add/',
        views.student_create,
        name='student_create'
    ),

    path(
        'edit/<int:pk>/',
        views.student_update,
        name='student_update'
    ),

    path(
        'delete/<int:pk>/',
        views.student_delete,
        name='student_delete'
    ),
    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

]
