from blog_app.models import Author, Category, Post
from django.test import TestCase


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(name="Test Author", email="author@test.com")

    def test_author_str(self):
        author = Author.objects.get(name="Test Author")
        self.assertEqual(str(author), "Test Author")


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Test Category")

    def test_category_str(self):
        category = Category.objects.get(name="Test Category")
        self.assertEqual(str(category), "Test Category")


class PostTestCase(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Test Author", email="author@test.com")

        post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=author
        )
        post.categories.set(
            [
                Category.objects.create(name="c1"),
            ]
        )

        post = Post.objects.create(
            title="Test Post appears", content="This is a c2 test post.", author=author
        )
        post.categories.set(
            [
                Category.objects.create(name="c2"),
            ]
        )

    def test_post_str(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(str(post), "Test Post")

    def test_post_num_words(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.num_words, 5)
        post.content = "This is a test post with more words."
        post.save()
        self.assertEqual(post.num_words, 8)

    def test_post_did_category_not_appear(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.did_category_name_appear_in_post, False)

    def test_post_did_category_appear(self):
        post = Post.objects.get(title="Test Post appears")
        self.assertEqual(post.did_category_name_appear_in_post, True)

    def test_post_did_category_appear_on_content_change(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.did_category_name_appear_in_post, False)

        post.content = "This is a test post with c1 in the content."
        post.save()
        self.assertEqual(post.did_category_name_appear_in_post, True)

        post.content = "This is a test post."
        post.save()
        self.assertEqual(post.did_category_name_appear_in_post, False)

    def test_post_did_category_appear_on_categories_change(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.did_category_name_appear_in_post, False)

        post.categories.add(Category.objects.create(name="test"))
        post.save()
        self.assertEqual(post.did_category_name_appear_in_post, True)

        post.categories.remove(Category.objects.get(name="test"))
        post.save()
        self.assertEqual(post.did_category_name_appear_in_post, False)
