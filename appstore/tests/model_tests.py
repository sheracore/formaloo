from django.test import TestCase
from django.contrib.auth.models import User
from ..models import App, CategoryChoices, VerificationStatus
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

class AppModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='user1', password='password123')

    def test_create_app(self):
        app = App.objects.create(
            title='Test App',
            description='This is a test app description.',
            price=9.99,
            user=self.user,
            verification_status=VerificationStatus.PENDING,
            category=CategoryChoices.GAMES,
            version="1.0.0"
        )
        self.assertEqual(app.title, 'Test App')
        self.assertEqual(app.user.username, 'user1')
        self.assertEqual(app.verification_status, VerificationStatus.PENDING)
        self.assertEqual(app.price, 9.99)
        self.assertEqual(app.category, CategoryChoices.GAMES)

    def test_create_app_invalid_title_unique_constraint(self):
        # Create a valid app
        App.objects.create(
            title='Unique App',
            description='This is a test app description.',
            price=9.99,
            user=self.user,
            verification_status=VerificationStatus.PENDING,
            category=CategoryChoices.GAMES,
            version="1.0.0"
        )

        # Try to create another app with the same title (should raise IntegrityError)
        with self.assertRaises(IntegrityError):
            App.objects.create(
                title='Unique App',  # Same title
                description='This is another test app description.',
                price=9.99,
                user=self.user,
                verification_status=VerificationStatus.PENDING,
                category=CategoryChoices.SOCIAL,
                version="1.1.0"
            )

    def test_string_representation(self):
        # Test string representation of the app
        app = App.objects.create(
            title='String Test App',
            description='Testing string representation.',
            price=5.99,
            user=self.user,
            verification_status=VerificationStatus.PENDING,
            category=CategoryChoices.HEALTH,
            version="1.0.0"
        )
        self.assertEqual(str(app), 'String Test App - user1')

    def test_create_app_with_invalid_status(self):
        # Try creating an app with an invalid verification status
        with self.assertRaises(ValidationError): # TODO: does it get ValidationError??
            App.objects.create(
                title='Invalid Status App',
                description='App with invalid status.',
                price=6.00,
                user=self.user,
                verification_status=VerificationStatus.VERIFIED,  # Invalid status
                category=CategoryChoices.HEALTH,
                version="1.0.0"
            )

    def test_create_app_with_default_pending_status(self):
        # Ensure apps are created with default status as 'pending'
        app = App.objects.create(
            title='Default Status App',
            description='App with default status.',
            price=1.99,
            user=self.user,
            category=CategoryChoices.SOCIAL,
            version="1.0.0"
        )
        self.assertEqual(app.verification_status, VerificationStatus.PENDING)

