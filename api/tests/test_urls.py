from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.PostViews import post_list, post_detail
from api.AuthorViews import author_list, author_detail
from api.CategoryViews import category_list, category_detail


class TestPostUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("post-list")
        self.assertEqual(resolve(url).func, post_list)

    def test_detail_url_resolves(self):
        url = reverse("post-detail", args=[1])
        self.assertEqual(resolve(url).func, post_detail)


class TestAuthorUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("author-list")
        self.assertEqual(resolve(url).func, author_list)

    def test_detail_url_resolves(self):
        url = reverse("author-detail", args=[1])
        self.assertEqual(resolve(url).func, author_detail)


class TestCategoryUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("category-list")
        self.assertEqual(resolve(url).func, category_list)

    def test_detail_url_resolves(self):
        url = reverse("category-detail", args=[1])
        self.assertEqual(resolve(url).func, category_detail)
