from django.db import models
from django.db.models.signals import pre_save


class City(models.Model):
    city = models.CharField(
        max_length=255,
        verbose_name='город'
    )
    description = models.TextField()
    population = models.IntegerField()
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f'{self.city}'

        class Meta:
            ordering = ('-id',)


class CityImage(models.Model):
    image = models.ImageField(
        upload_to='city',
        verbose_name='Картинки',
        blank=True, null=True,
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE,
        related_name='city_image'
    )

    def __str__(self):
        return f"{self.city.city} -- {self.city.id}"


class University(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='univer'
    )
    university = models.CharField(
        max_length=255,
        verbose_name='унивеститет'
    )
    description = models.TextField()
    image = models.ImageField(
        verbose_name='Картинки',
        blank=True, null=True,
    )
    number_of_people = models.IntegerField(
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.university}--{self.city}"

        class Meta:
            ordering = ('-id',)
