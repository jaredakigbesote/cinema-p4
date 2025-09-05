import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from cinema.models import Movie, Screening, Booking
from django.utils import timezone


class ModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="A New Hope",
            description="Episode IV",
            duration=121
        )
        # screening_time: use timezone-aware future time
        self.screening = Screening.objects.create(
            movie=self.movie,
            screening_time=timezone.now() + datetime.timedelta(days=1),
            screen_number=1,
            seats=100,
        )
        self.user = get_user_model().objects.create_user(
            username="luke", password="force"
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "A New Hope")

    def test_screening_str(self):
        # Adjust if your __str__ is different
        self.assertIn("A New Hope", str(self.screening))
        self.assertIn("Screen", str(self.screening))

    def test_booking_create_and_str(self):
        booking = Booking.objects.create(
            user=self.user,
            screening=self.screening,
            seats_booked=2
        )
        self.assertEqual(Booking.objects.count(), 1)
        self.assertIn("A New Hope", str(booking))
        self.assertIn("luke", str(booking))
