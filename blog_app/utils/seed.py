from blog_app.models import Author, Category, Post
import random
from blog_app.utils.author_data import get_author_data
from blog_app.utils.post_data import get_post_data
from blog_app.utils.category_data import get_category_data


def seed_categories():
    categories = get_category_data()

    categories = Category.objects.bulk_create(
        [Category(name=category) for category in categories]
    )
    return categories


def seed_authors():
    authors = get_author_data()

    authors = Author.objects.bulk_create([Author(**author) for author in authors])
    return authors


def seed_posts(n):
    posts = [Post(**get_post_data()) for _ in range(n)]

    authors = Author.objects.all()
    for post in posts:
        post.author = random.choice(authors)

    posts = Post.objects.bulk_create(posts)

    # m2m relationships
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

    return posts


def seed(n_posts):
    categories = seed_categories()
    authors = seed_authors()
    posts = seed_posts(n_posts)

    return categories, authors, posts
