# Generated by Django 4.1.2 on 2023-02-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinprofile',
            name='development_status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
