from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog_app.models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def list_blogs(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
