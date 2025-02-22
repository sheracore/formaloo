from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import App, CategoryChoices


class AppCreationTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up test data once for the entire test class."""
        cls.user = User.objects.create_user(username="testuser", password="password123")
        cls.valid_payload = {
            "title": "My First App",
            "description": "This is a test app",
            "price": 9.99,
            "category": CategoryChoices.GAMES,
            "version": "1.0.0"
        }

    def setUp(self):
        """Runs before each test. Authenticates the test client."""
        self.client.force_authenticate(user=self.user)

    def test_create_app_successfully(self):
        """Test that an authenticated user can successfully create an app."""
        response = self.client.post("/apps", self.valid_payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(App.objects.count(), 1)
        self.assertEqual(App.objects.first().title, "My First App")
        self.assertEqual(App.objects.first().user, self.user)

    def test_create_app_unauthenticated_fails(self):
        """Test that unauthenticated users cannot create an app."""
        self.client.logout()
        response = self.client.post("/apps", self.valid_payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_app_missing_fields_fails(self):
        """Test that missing required fields return a validation error."""
        invalid_payload = {
            "description": "Missing title and price"
        }
        response = self.client.post("/apps", invalid_payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_create_app_invalid_price_fails(self):
        """Test that providing an invalid price returns a validation error."""
        invalid_payload = self.valid_payload.copy()
        invalid_payload["price"] = "invalid_price"

        response = self.client.post("/apps", invalid_payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("price", response.data)
