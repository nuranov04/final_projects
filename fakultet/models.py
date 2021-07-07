from django.db import models
from cities.models import University
from django.db.models.signals import pre_save
# from utils.slug_generator import unique_slug_generators


class Faculty(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='faculty'
    )
    faculty = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.faculty}---{self.university}"

    class Meta:
        ordering = ('-id',)


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Faculty)
