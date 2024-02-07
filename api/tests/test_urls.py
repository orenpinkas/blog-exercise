from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import post_list, post_detail


class TestUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("post-list")
        self.assertEqual(resolve(url).func, post_list)

    def test_detail_url(self):
        url = reverse("post-detail", args=[1])
        self.assertEqual(resolve(url).func, post_detail)
