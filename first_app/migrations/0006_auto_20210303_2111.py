# Generated by Django 3.1.7 on 2021-03-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_personsprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='personsprofile',
            name='phone_no',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
