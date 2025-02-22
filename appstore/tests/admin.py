from django.contrib.auth.models import User
from django.test import TestCase, Client
from ..models import App, VerificationStatus


class AdminAppVerificationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up test data: create an admin user, a regular user, and some apps."""
        cls.client = Client()
        cls.admin_user = User.objects.create_superuser(username="admin", password="admin123")
        cls.user = User.objects.create_user(username="user", password="user123")
        cls.app1 = App.objects.create(
            user=cls.user, title="Pending App1", description="Test App1", price="0.99",
            category=1, version="1.0.0", verification_status=VerificationStatus.PENDING
        )
        cls.app2 = App.objects.create(
            user=cls.user, title="Pending App2", description="Test App2", price="0.99",
            category=1, version="1.0.0", verification_status=VerificationStatus.PENDING
        )
        cls.app3 = App.objects.create(
            user=cls.user, title="Pending App3", description="Test App3", price="0.99",
            category=1, version="1.0.0", verification_status=VerificationStatus.PENDING
        )

    def setUp(self):
        """Log in as admin before each test."""
        self.client.login(username="admin", password="admin123")

    def test_admin_can_mark_as_verified(self):
        """Test that the admin action correctly marks selected apps as VERIFIED."""
        self.client.post("/admin/appstore/app/", {
            "action": "mark_as_verified",
            "_selected_action": [self.app1.id]
        })
        self.app1.refresh_from_db()
        self.assertEqual(self.app1.verification_status, VerificationStatus.VERIFIED)

    def test_admin_can_mark_as_rejected(self):
        """Test that the admin action correctly marks selected apps as REJECTED."""
        self.client.post("/admin/appstore/app/", {
            "action": "mark_as_rejected",
            "_selected_action": [self.app2.id]
        })
        self.app2.refresh_from_db()
        self.assertEqual(self.app2.verification_status, VerificationStatus.REJECTED)

    def test_admin_can_mark_as_pending(self):
        """Test that the admin action correctly marks selected apps as PENDING."""
        self.client.post("/admin/appstore/app/", {
            "action": "mark_as_pending",
            "_selected_action": [self.app3.id]
        })
        self.app3.refresh_from_db()
        self.assertEqual(self.app3.verification_status, VerificationStatus.PENDING)

    def test_admin_list_filter_verification_status(self):
        """Test that the admin panel filters apps by verification status."""
        response = self.client.get("/admin/appstore/app/?verification_status__exact=3")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pending App")
        self.assertNotContains(response, "Rejected App")
        self.assertNotContains(response, "Verified App")

    def test_admin_requires_login(self):
        """Test that accessing the admin panel without login redirects to login page."""
        self.client.logout()
        response = self.client.get("/admin/appstore/app/")
        self.assertEqual(response.status_code, 302)

    def test_non_admin_cannot_access_admin_panel(self):
        """Test that a non-admin user cannot access the admin panel."""
        self.client.logout()
        self.client.login(username="user", password="user123")
        response = self.client.get("/admin/appstore/app/")
        self.assertEqual(response.status_code, 302)

