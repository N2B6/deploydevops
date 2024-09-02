"""Defines the models for the Wanderlust app."""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class WanderlustUser(AbstractUser):
    """
    Custom user model for the Wanderlust app.

    Inherits from Django's AbstractUser model and adds custom fields.
    """

    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(_("phone number"), max_length=15, null=True, blank=True)
    dob = models.DateField(_("date of birth"), null=True, blank=True)

    # Meta class to specify custom permissions
    class Meta:
        """
        Meta options for the WanderlustUser model.

        Specifies the name of the model and a custom permission.
        """

        permissions = (("can_access_dashboard", "Can access dashboard"),)

    # Overriding the save method to handle custom logic
    def save(self, *args, **kwargs):
        """
        Save the user instance with custom logic.

        Sets the username field to the email address if it is not set.
        """
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return the username of the user.

        Used for string representation of the user object.
        """
        return self.username

class Trip(models.Model):
    """
    Model for a trip.

    Represents a trip with various attributes, such as title, description, start and end dates,
    destination, travel mode, accommodation type, estimated budget, and participants.
    """

    user = models.ForeignKey(WanderlustUser, on_delete=models.CASCADE)
    image = models.ImageField(_("trip image"), upload_to="trip_images/", null=True, blank=True)
    title = models.CharField(_("trip title"), max_length=100)
    description = models.TextField(_("trip description"))
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    destination = models.CharField(_("destination"), max_length=255)
    travel_mode = models.CharField(_("travel mode"), max_length=50, choices=[
        ('AIRPLANE', _("Airplane")),
        ('CAR', _("Car")),
        ('TRAIN', _("Train")),
        ('BUS', _("Bus")),
        ('CRUISE', _("Cruise")),
        ('WALK', _("Walk")),
        ('MULTIPLE', _("Multiple")),
    ])
    accommodation_type = models.CharField(_("accommodation type"), max_length=50, choices=[
        ('HOTEL', _("Hotel")),
        ('HOSTEL', _("Hostel")),
        ('AIRBNB', _("Airbnb")),
        ('CAMPSITE', _("Campsite")),
        ('OTHER', _("Other")),
    ])
    estimated_budget = models.DecimalField(_("estimated budget"), max_digits=10, decimal_places=2,
                                           null=True, blank=True)
    participants = models.ManyToManyField(WanderlustUser, related_name="joined_trips", blank=True)
    max_participants = models.PositiveIntegerField(_("maximum participants"), null=True, blank=True)

    def __str__(self) -> str:
        """
        Return the title of the trip.

        Used for string representation of the trip object.
        """
        return str(self.title or "Trip (no title)")
