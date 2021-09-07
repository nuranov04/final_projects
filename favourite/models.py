from django.db import models
from cities.models import University
from users.models import User

class Favourite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_favourite'
    )
    university = models.ManyToManyField(
        University,
        related_name='university_favourite'
    )

    def __str__(self):
        return f"{self.user.username}--{self.university.university}"