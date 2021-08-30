from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.files import ImageField


class User(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'Men'),
        ('f', 'Female'),
        ("I don't know", 'Trans'),
    )
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    profile = models.ImageField(upload_to='profiles', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)

    def __str__(self) -> str:
        return f"{self.username}--{self.id}"
