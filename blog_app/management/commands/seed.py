from blog_app.models import Author, Category, Post
from django.core.management.base import BaseCommand, CommandParser
import random
from faker import Faker
from blog_app.utils.authors import get_authors


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
        post_categories = random.sample(categories, random.randint(1, 3))
        post.categories.set(post_categories)
        if random.choice([True, False]):
            post.content += " " + post_categories[0].name
        post.did_category_name_appear_in_post = any(
            category.name in post.content for category in post_categories
        )

    Post.objects.bulk_update(posts, ["content", "did_category_name_appear_in_post"])


def generate_post_data(authors):
    fake = Faker()
    title = (
        f"{fake.catch_phrase()} {random.choice(['Tips', 'Tricks', 'Guide', 'Ideas'])}"
    )
    content = fake.text(
        max_nb_chars=1000
    )  # Generates random text up to 1000 characters
    author = random.choice(authors)
    return {
        "title": title,
        "content": content,
        "author": author,
        "num_words": len(content.split()),
    }


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def add_arguments(self, parser: CommandParser) -> None:
        # Positional arguments
        parser.add_argument("n_posts", type=str, help="number of posts to create")

    def validate_argument(self, n_posts):
        try:
            n_posts = int(n_posts)
        except ValueError:
            raise ValueError("n_posts must be a number")

        if n_posts < 1:
            raise ValueError("n_posts must be greater than 0")

        if n_posts > 10000:
            raise ValueError("n_posts must be less than 10000")

    def handle(self, *args, **options):
        try:
            self.validate_argument(options["n_posts"])
        except ValueError as e:
            self.stdout.write(self.style.ERROR(str(e)))
            return
        n_posts = int(options["n_posts"])

        if Post.objects.exists():
            print("Posts already exist in the database. Aborting seeding.")
            return

        print(f"Seeding database with {n_posts} posts...")

        seed_categories()
        seed_authors()
        seed_posts(n_posts)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
