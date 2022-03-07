from locale import currency
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_MAIL = "male"
    GENDER_FEMAIL = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = (
        (GENDER_FEMAIL, "Female"),
        (GENDER_MAIL, "Male"),
        (GENDER_OTHER, "Other")
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE,
                              max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=20, null=True, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    superhost = models.BooleanField(default=False)
