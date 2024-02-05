from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog_app.models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def list_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PATCH"])
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response("Post deleted successfully")
