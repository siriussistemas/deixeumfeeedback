from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DjangoUserManager


class UserManager(DjangoUserManager["User"]):
    def _create_user(self, email: str, password: str | None, **extra_fields):
        if not email:
            msg = "The given email must be set"
            raise ValueError(msg)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str | None = None, **extra_fields):  # type: ignore[override]
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str | None = None, **extra_fields):  # type: ignore[override]
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("username"):
            extra_fields.setdefault("username", email)

        if extra_fields.get("is_staff") is not True:
            msg = "Superuser must have is_staff=True."
            raise ValueError(msg)
        if extra_fields.get("is_superuser") is not True:
            msg = "Superuser must have is_superuser=True."
            raise ValueError(msg)

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    name = models.CharField("name", max_length=255, blank=True)
    username = models.CharField("username", max_length=255, unique=True)
    email = models.EmailField("email address", unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def create_api_key(self):
        return ApiKey.objects.create(user=self)


class ApiKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="api_keys")
    apiKey = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.apiKey
