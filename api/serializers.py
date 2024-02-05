from rest_framework import serializers
from blog_app.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'categories', 'created_at')
