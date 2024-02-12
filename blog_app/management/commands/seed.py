from blog_app.models import Post
from blog_app.utils.seed import seed
from django.core.management.base import BaseCommand, CommandParser


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

        seed(n_posts=n_posts)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
