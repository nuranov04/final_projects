# Generated by Django 3.2.4 on 2021-08-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultet', '0003_alter_application_number_of_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='number_of_phone',
            field=models.IntegerField(max_length=13),
        ),
    ]
