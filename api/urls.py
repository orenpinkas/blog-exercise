from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.list_posts),
    path("create/", views.create_post),
    path("update/<int:pk>/", views.update_post),
    path("delete/<int:pk>/", views.delete_post),
]
