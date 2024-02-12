from django.test import Client, TestCase
from blog_app.models import Author, Category, Post
from blog_app.utils.seed import seed


class TestPostViews(TestCase):
    def compare_post_data(self, post, received_post):
        self.assertEqual(post.id, received_post["id"])
        self.assertEqual(post.title, received_post["title"])
        self.assertEqual(post.content, received_post["content"])
        self.assertEqual(post.author.id, received_post["author"])
        self.assertEqual(
            [category.id for category in post.categories.all()],
            received_post["categories"],
        )

    def setUp(self):
        self.client = Client()
        self.categories, self.authors, self.posts = seed(n_posts=5)

    def test_post_list_get(self):
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)

        received_posts = response.json()
        for post, received_post in zip(self.posts, received_posts):
            self.compare_post_data(post, received_post)

    def test_post_list_post(self):
        data = {
            "title": "New Post",
            "content": "This is a new post.",
            "author": self.authors[0].id,
            "categories": [self.categories[0].id],
        }
        self.assertFalse(Post.objects.filter(title="New Post").exists())

        response = self.client.post(
            "/api/posts/", data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Post.objects.filter(title="New Post").exists())

    def test_post_detail_get(self):
        post = self.posts[0]
        response = self.client.get(f"/api/posts/{post.id}/")
        self.assertEqual(response.status_code, 200)

        received_post = response.json()
        self.compare_post_data(post, received_post)

    def test_post_detail_put(self):
        post = self.posts[0]
        data = {
            "title": "Updated Post",
            "content": "This is an updated post.",
            "author": self.authors[0].id,
            "categories": [self.categories[0].id],
        }
        response = self.client.put(
            f"/api/posts/{post.id}/", data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

        post.refresh_from_db()
        received_post = response.json()
        self.compare_post_data(post, received_post)

    def test_post_detail_post(self):
        data = {
            "title": "New Post",
            "content": "This is a new post.",
            "author": self.authors[0].id,
            "categories": [self.categories[0].id],
        }
        self.assertFalse(Post.objects.filter(title="New Post").exists())

        response = self.client.post(
            f"/api/posts/{self.posts[0].id}/", data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Post.objects.filter(title="New Post").exists())

    def test_post_detail_delete(self):
        post = self.posts[0]
        self.assertTrue(Post.objects.filter(id=post.id).exists())

        response = self.client.delete(f"/api/posts/{post.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Post.objects.filter(id=post.id).exists())


class TestAuthorViews(TestCase):
    def compare_author_data(self, author, received_author):
        self.assertEqual(author.id, received_author["id"])
        self.assertEqual(author.name, received_author["name"])
        self.assertEqual(author.email, received_author["email"])

    def setUp(self):
        self.client = Client()
        self.categories, self.authors, self.posts = seed(n_posts=0)

    def test_author_list_get(self):
        response = self.client.get("/api/authors/")
        self.assertEqual(response.status_code, 200)

        received_authors = response.json()
        for author, received_author in zip(self.authors, received_authors):
            self.compare_author_data(author, received_author)

    def test_author_list_post(self):
        data = {"name": "New Author", "email": "new@author.com"}
        self.assertFalse(Author.objects.filter(name="New Author").exists())

        response = self.client.post(
            "/api/authors/", data, content_type="application/json"
        )
        self.assertTrue(response.status_code, 201)
        self.assertTrue(Author.objects.filter(name="New Author").exists())

    def test_author_detail_get(self):
        author = self.authors[0]
        response = self.client.get(f"/api/authors/{author.id}/")
        self.assertEqual(response.status_code, 200)

        received_author = response.json()
        self.compare_author_data(author, received_author)

    def test_author_detail_put(self):
        author = self.authors[0]
        data = {"name": "Updated Author", "email": "new@author.com"}

        response = self.client.put(
            f"/api/authors/{author.id}/", data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

        author.refresh_from_db()
        received_author = response.json()
        self.compare_author_data(author, received_author)

    def test_author_detail_post(self):
        data = {"name": "New Author", "email": "new@author.com"}
        self.assertFalse(Author.objects.filter(name="New Author").exists())

        response = self.client.post(
            f"/api/authors/{self.authors[0].id}/", data, content_type="application/json"
        )
        self.assertTrue(response.status_code, 201)
        self.assertTrue(Author.objects.filter(name="New Author").exists())

    def test_author_detail_delete(self):
        author = self.authors[0]
        self.assertTrue(Author.objects.filter(id=author.id).exists())

        response = self.client.delete(f"/api/authors/{author.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Author.objects.filter(id=author.id).exists())


class TestCategoryViews(TestCase):
    def compare_category_data(self, category, received_category):
        self.assertEqual(category.id, received_category["id"])
        self.assertEqual(category.name, received_category["name"])

    def setUp(self):
        self.client = Client()
        self.categories, self.authors, self.posts = seed(n_posts=0)

    def test_category_list_get(self):
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, 200)

        received_categories = response.json()
        for category, received_category in zip(self.categories, received_categories):
            self.compare_category_data(category, received_category)

    def test_category_list_post(self):
        data = {"name": "New Category"}
        self.assertFalse(Category.objects.filter(name="New Category").exists())

        response = self.client.post(
            "/api/categories/", data, content_type="application/json"
        )
        self.assertTrue(response.status_code, 201)
        self.assertTrue(Category.objects.filter(name="New Category").exists())

    def test_category_detail_get(self):
        category = self.categories[0]
        response = self.client.get(f"/api/categories/{category.id}/")
        self.assertEqual(response.status_code, 200)

        received_category = response.json()
        self.compare_category_data(category, received_category)

    def test_category_detail_put(self):
        category = self.categories[0]
        data = {"name": "Updated Category"}

        response = self.client.put(
            f"/api/categories/{category.id}/", data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

        category.refresh_from_db()
        received_category = response.json()
        self.compare_category_data(category, received_category)

    def test_category_detail_post(self):
        data = {"name": "New Category"}
        self.assertFalse(Category.objects.filter(name="New Category").exists())

        response = self.client.post(
            f"/api/categories/{self.categories[0].id}/",
            data,
            content_type="application/json",
        )
        self.assertTrue(response.status_code, 201)
        self.assertTrue(Category.objects.filter(name="New Category").exists())

    def test_category_detail_delete(self):
        category = self.categories[0]
        self.assertTrue(Category.objects.filter(id=category.id).exists())

        response = self.client.delete(f"/api/categories/{category.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Category.objects.filter(id=category.id).exists())
