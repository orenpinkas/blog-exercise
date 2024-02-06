from blog_app.models import Author, Category, Post
from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from faker import Faker
from blog_app.utils.authors import get_authors
import time


def seed_categories():
    categories = [
        "Science",
        "Technology",
        "Politics",
        "Sports",
        "Health",
        "Entertainment",
        "Travel",
        "Food",
        "Fashion",
        "Lifestyle",
    ]

    categories = Category.objects.bulk_create(
        [Category(name=category) for category in categories]
    )
    return categories


def seed_authors():
    authors = get_authors()

    authors = Author.objects.bulk_create([Author(**author) for author in authors])
    return authors


def seed_posts(n):
    authors = Author.objects.all()
    posts = [Post(**generate_post_data(authors)) for _ in range(n)]

    posts = Post.objects.bulk_create(posts)

    categories = list(Category.objects.all())
    for post in posts:
        post.categories.set(random.sample(categories, random.randint(1, 3)))


def generate_post_data(authors):
    fake = Faker()
    title = (
        f"{fake.catch_phrase()} {random.choice(['Tips', 'Tricks', 'Guide', 'Ideas'])}"
    )
    content = fake.text(
        max_nb_chars=1000
    )  # Generates random text up to 1000 characters
    author = random.choice(authors)
    return {"title": title, "content": content, "author": author}


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **options):
        seed_categories()
        seed_authors()
        seed_posts(10000)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
