from django.db import models
from cities.models import University
from django.db.models.signals import pre_save


# from utils.slug_generator import unique_slug_generators


class Faculty(models.Model):
    CHOICES_CART = (
        ('o', 'Open'),
        ('c', 'Close')
    )

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='faculty'
    )
    faculty = models.CharField(
        max_length=255,

    )

    description = models.TextField()
    price = models.IntegerField()
    open_or_close = models.CharField(choices=CHOICES_CART, max_length=15)

    def __str__(self):
        return f"{self.university}--{self.faculty}"

    class Meta:
        ordering = ('-id',)


