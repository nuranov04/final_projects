# Generated by Django 3.2.4 on 2021-07-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0010_university_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинки'),
        ),
    ]
