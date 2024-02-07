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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = str(instance.author)
        representation["categories"] = [
            str(category) for category in instance.categories.all()
        ]
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "email"]
