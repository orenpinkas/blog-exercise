from django.db import models
from django.utils.timezone import make_aware
from dateutil import parser


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    def created_between(self, posts, start, end):
        try:
            if start is None:
                end = make_aware(parser.parse(end))
                return posts.filter(created_at__lte=end)
            elif end is None:
                start = make_aware(parser.parse(start))
                return posts.filter(created_at__gte=start)
            else:
                start = make_aware(parser.parse(start))
                end = make_aware(parser.parse(end))
                return posts.filter(created_at__range=(start, end))
        except (TypeError, parser._parser.ParserError):
            return posts

    def of_category(self, posts, category):
        try:
            return posts.filter(categories__name=category)
        except Category.DoesNotExist:
            return posts

    def custom_filter(self, **kwargs):
        posts = self.get_queryset()
        posts = self.created_between(
            posts, start=kwargs.get("start"), end=kwargs.get("end")
        )
        posts = self.of_category(posts, category=kwargs.get("category"))
        return posts


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title
