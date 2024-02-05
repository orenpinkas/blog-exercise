from blog_app.models import Author, Category, Post
from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from faker import Faker

def seed_categories():
    categories = ["Science", "Technology", "Politics", "Sports", "Health", "Entertainment", "Travel", "Food", "Fashion", "Lifestyle"]
    categories = map(lambda category: {"name": category}, categories)

    categories = [Category.objects.get_or_create(**category)[0] for category in categories]
    return categories

def seed_authors():
    authors = [
            {
                "name": "John Doe",
                "email": "john.doe@blogs.com"
            },
            {
                "name": "Jane Doe",
                "email": "jane.doe@blogs.com"
            },
            {
                "name": "oren pinkas",
                "email": "oren@blogs.com"
            },
        ]
    
    authors = [Author.objects.get_or_create(**author)[0] for author in authors]
    return authors

def seed_posts(n, all_authors, all_categories):
    posts = [generate_post(all_authors, all_categories) for _ in range(n)]
    for title, content, author, categories in posts:
        post = Post(title=title, content=content, author=author)
        post.save()
        post.categories.set(categories)

def generate_post(all_authors, all_categories):
    fake = Faker()
    title = f"{fake.catch_phrase()} {random.choice(['Tips', 'Tricks', 'Guide', 'Ideas'])}"
    content = fake.text(max_nb_chars=1000)  # Generates random text up to 1000 characters
    author = random.choice(all_authors)
    categories = random.choices(all_categories, k=random.randint(1, 3))
    print(categories)
    return title, content, author, categories


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):

        authors = seed_authors()
        categories = seed_categories()
        seed_posts(12, authors, categories)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
