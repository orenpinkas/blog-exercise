from rest_framework import serializers
from blog_app.models import Post, Author, Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )

    class Meta:
        model = Post
        fields = ["title", "content", "author", "categories", "created_at"]
