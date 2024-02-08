from django.urls import path
from . import PostViews, AuthorViews, CategoryViews

urlpatterns = [
    path("posts/", PostViews.post_list, name="post-list"),
    path("posts/<int:pk>/", PostViews.post_detail, name="post-detail"),
    path("categories/", CategoryViews.category_list, name="category-list"),
    path("categories/<int:pk>/", CategoryViews.category_detail, name="category-detail"),
    path("authors/", AuthorViews.author_list, name="author-list"),
    path("authors/<int:pk>/", AuthorViews.author_detail, name="author-detail"),
]
