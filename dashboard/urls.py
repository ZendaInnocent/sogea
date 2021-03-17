from django.urls import path

from .import views

app_name = 'dashboard'

urlpatterns = [
   path('posts/', views.dashboard, name='dashboard'),
   path('profile/<int:id>/edit/', views.profile_update, name='profile_update'),
]