from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AuthTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="leia", password="resistance"
        )

    def test_login_page_renders(self):
        # Adjust if you use a custom route
        resp = self.client.get(reverse("login"))
        self.assertEqual(resp.status_code, 200)

    def test_can_login(self):
        logged_in = self.client.login(username="leia", password="resistance")
        self.assertTrue(logged_in)

    def test_logout(self):
        self.client.login(username="leia", password="resistance")
        resp = self.client.get(reverse("logout"))
        self.assertIn(resp.status_code, (200, 302))
