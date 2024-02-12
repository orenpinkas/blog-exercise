from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    num_words = models.IntegerField(blank=True, null=True)
    did_category_name_appear_in_post = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        words = self.content.split()
        self.num_words = len(words)
        if self.id:  # if the post is already saved
            self.did_category_name_appear_in_post = any(
                category.name in words for category in self.categories.all()
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(m2m_changed, sender=Post.categories.through)
def categories_changed_receiver(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for pk in pk_set:
            category = Category.objects.get(pk=pk)
            if category.name in instance.content:
                instance.did_category_name_appear_in_post = True
                instance.save(update_fields=["did_category_name_appear_in_post"])
                break
        instance.did_category_name_appear_in_post = False
