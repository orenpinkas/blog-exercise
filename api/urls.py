from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.post_list),
    path("posts/<int:pk>/", views.post_detail),
    path("categories/", views.category_list),
    path("categories/<int:pk>/", views.category_detail),
    path("authors/", views.author_list),
    path("authors/<int:pk>/", views.author_detail),
]
