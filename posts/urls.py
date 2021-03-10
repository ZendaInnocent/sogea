from django.urls import path

from .import views

app_name = 'posts'

urlpatterns = [
    path('write-post/', views.create_edit_post, name='create_post'),
    path('<int:id>/edit/', views.create_edit_post, name="edit_post"),
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
    path('save-post-bookmark/', views.save_post_bookmark, name='save_post_bookmark'),
    path('follow/', views.follow_profile, name='follow_profile'),
]