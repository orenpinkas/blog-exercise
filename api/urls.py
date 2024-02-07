from django.urls import path
from . import PostViews, AuthorViews, CategoryViews

urlpatterns = [
    path("posts/", PostViews.post_list),
    path("posts/<int:pk>/", PostViews.post_detail),
    path("categories/", CategoryViews.category_list),
    path("categories/<int:pk>/", CategoryViews.category_detail),
    path("authors/", AuthorViews.author_list),
    path("authors/<int:pk>/", AuthorViews.author_detail),
]
