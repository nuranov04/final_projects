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


class Application(models.Model):
    email = models.EmailField()
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name='application_faculty'
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number_of_phone = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.email}--{self.first_name}"

    
