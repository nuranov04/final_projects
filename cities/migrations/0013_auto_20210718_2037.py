# Generated by Django 3.2.4 on 2021-07-18 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0012_remove_city_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='image',
        ),
        migrations.CreateModel(
            name='UniversityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='city', verbose_name='Картинки')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_image', to='cities.university')),
            ],
        ),
    ]
