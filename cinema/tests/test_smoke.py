from django.test import TestCase
from django.urls import reverse

class SmokeTests(TestCase):
    def test_movie_list_url_name_exists(self):
        # Change "movie_list" if your url name is different
        url = reverse("movie_list")
        self.assertTrue(url)
