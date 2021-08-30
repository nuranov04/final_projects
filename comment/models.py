from django.db import models
from cities.models import City, University
from users.models import User


class CommentCity(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User, 
        related_name='user_city_comments', 
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City,
        related_name='city_comments',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.user.id}--{self.city.id}"

class CommentUniversity(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User, 
        related_name='user_comments', 
        on_delete=models.CASCADE
    )
    university = models.ForeignKey(
        University,
        related_name='university_comments',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.user.id}--{self.university.id}"
    
