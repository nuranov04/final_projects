# Generated by Django 3.2.4 on 2021-07-02 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakultet', '0002_auto_20210702_0907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ('-id',)},
        ),
    ]
