from django.urls import path
from . import author_views, category_views, post_views

urlpatterns = [
    path("posts/", post_views.post_list, name="post-list"),
    path("posts/<int:pk>/", post_views.post_detail, name="post-detail"),
    path("categories/", category_views.category_list, name="category-list"),
    path(
        "categories/<int:pk>/", category_views.category_detail, name="category-detail"
    ),
    path("authors/", author_views.author_list, name="author-list"),
    path("authors/<int:pk>/", author_views.author_detail, name="author-detail"),
]
