from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blog_app.models import Author
from .serializers import AuthorSerializer


@csrf_exempt
def author_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(author, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        author.delete()
        return HttpResponse(status=204)
