from django.db import models
from django.contrib.auth.models import User


class CategoryChoices(models.IntegerChoices):
    GAMES = 1, "Games"
    PRODUCTIVITY = 2, "Productivity"
    SOCIAL = 3, "Social"
    EDUCATION = 4, "Education"
    HEALTH = 5, "Health"
    OTHER = 6, "Other"

class VerificationStatus(models.TextChoices):
    VERIFIED = 'verified', 'Verified'
    REJECTED = 'rejected', 'Rejected'
    PENDING = 'pending', 'Pending'


class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apps")
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="In US dollars")
    verification_status = models.CharField(
        max_length=16,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING
    )
    category = models.IntegerField(choices=CategoryChoices.choices, default=CategoryChoices.OTHER)
    version = models.CharField(max_length=16, default="1.0.0")
    created_at = models.DateTimeField(auto_now_add=True) # TODO: Can moved to an abstract model
    updated_at = models.DateTimeField(auto_now=True) # TODO: Can moved to an abstract model
    """
    TODO fields:
        - icon field
    """

    class Meta:
        indexes = [
            models.Index(fields=['user']), # See the apps created by other users.
            models.Index(fields=['verification_status']), # For the admin panel (e.g., "pending verification").
            models.Index(fields=['category']),
            models.Index(fields=['verification_status', 'user']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.title} - {self.user.username}"