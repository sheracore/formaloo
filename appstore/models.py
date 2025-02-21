from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CategoryChoices(models.IntegerChoices):
    GAMES = 1, "Games"
    PRODUCTIVITY = 2, "Productivity"
    SOCIAL = 3, "Social"
    EDUCATION = 4, "Education"
    HEALTH = 5, "Health"
    OTHER = 6, "Other"


class VerificationStatus(models.IntegerChoices):
    VERIFIED = 1, 'Verified'
    REJECTED = 2, 'Rejected'
    PENDING = 3, 'Pending'


class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apps")
    title = models.CharField(max_length=255, unique=True)  # If unique=False the we need constraints(user, title)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="In US dollars")
    verification_status = models.IntegerField(
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING
    )
    category = models.IntegerField(choices=CategoryChoices.choices, default=CategoryChoices.OTHER)
    version = models.CharField(max_length=16, default="1.0.0")
    created_at = models.DateTimeField(auto_now_add=True)  # TODO: Can moved to an abstract model
    updated_at = models.DateTimeField(auto_now=True)  # TODO: Can moved to an abstract model
    """
    TODO fields:
        - icon field
    """

    class Meta:
        indexes = [
            models.Index(fields=['user']),  # See the apps created by other users.
            models.Index(fields=['verification_status']),  # For the admin panel (e.g., "pending verification").
            models.Index(fields=['category']),
            models.Index(fields=['verification_status', 'user']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.pk and self.verification_status != VerificationStatus.PENDING:
            raise ValidationError(
                {"verification_status": _("verification_status should be set to PENDING at creation process")})
        super().save(*args, **kwargs)
