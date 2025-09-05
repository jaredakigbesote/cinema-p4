import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from cinema.models import Movie, Screening, Booking


class PublicViewTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Empire Strikes Back",
            description="Episode V",
            duration=124
        )
        self.screening = Screening.objects.create(
            movie=self.movie,
            screening_time=timezone.now() + datetime.timedelta(days=1),
            screen_number=2,
            seats=150
        )

    def test_movie_list_page_loads(self):
        resp = self.client.get(reverse("movie_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Empire Strikes Back")

    def test_movie_detail_page_loads(self):
        resp = self.client.get(reverse("movie_detail", args=[self.movie.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Episode V")

    def test_booking_requires_login(self):
        # should redirect to login with next=
        resp = self.client.get(reverse("book_screening", args=[self.screening.id]))
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/accounts/login", resp.headers.get("Location", ""))


class PrivateViewTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Return of the Jedi",
            description="Episode VI",
            duration=131
        )
        self.screening = Screening.objects.create(
            movie=self.movie,
            screening_time=timezone.now() + datetime.timedelta(days=2),
            screen_number=3,
            seats=120
        )
        self.user = get_user_model().objects.create_user(
            username="han", password="solo"
        )
        self.client.login(username="han", password="solo")

    def test_book_screening_get(self):
        resp = self.client.get(reverse("book_screening", args=[self.screening.id]))
        self.assertEqual(resp.status_code, 200)
        # look for form fields – adjust names if different
        self.assertContains(resp, "name=\"seats_booked\"")

    def test_book_screening_post_creates_booking(self):
        resp = self.client.post(
            reverse("book_screening", args=[self.screening.id]),
            data={"seats_booked": 3}
        )
        # after a successful POST, you likely redirect back to details/home
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.screening, self.screening)
        self.assertEqual(booking.seats_booked, 3)
