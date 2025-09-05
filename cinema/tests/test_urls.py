from django.test import SimpleTestCase
from django.urls import resolve, reverse
from cinema import views


class UrlTests(SimpleTestCase):
    def test_movie_list_url(self):
        url = reverse("movie_list")
        self.assertEqual(resolve(url).func, views.movie_list_view)

    def test_movie_detail_url(self):
        url = reverse("movie_detail", kwargs={"movie_id": 1})
        self.assertEqual(resolve(url).func, views.movie_detail_view)

    def test_book_screening_url(self):
        url = reverse("book_screening", kwargs={"screening_id": 1})
        self.assertEqual(resolve(url).func, views.book_screening_view)
