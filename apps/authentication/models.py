from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import CustomUserManager

MALE = "Male"
FEMALE = "Female"

GENDER_CHOICE = (
    (MALE, MALE),
    (FEMALE, FEMALE),
)


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    lga = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )

    nationality = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )

    email = models.EmailField(
        unique=True,
        max_length=200,
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    address = models.TextField(
        blank=True,
        null=True,
    )

    occupation = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        to="service.ServiceUnit",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    marital_status = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )

    next_of_kin = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )

    nok_address = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )

    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["phone"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "CustomUser"

        verbose_name_plural = "CustomUsers"

        ordering = ["-id"]

    def __str__(self):
        return f"{self.get_full_name()}"
