# Generated by Django 4.1.2 on 2023-02-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinprofile',
            name='hardware_wallet',
            field=models.BooleanField(),
        ),
    ]