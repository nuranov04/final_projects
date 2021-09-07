# Generated by Django 3.2.4 on 2021-09-03 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_options'),
        ('favourite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='university',
        ),
        migrations.AddField(
            model_name='favourite',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='university_favourite', to='cities.university'),
            preserve_default=False,
        ),
    ]
