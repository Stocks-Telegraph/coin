# Generated by Django 4.1.2 on 2023-03-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_profile', '0003_alter_coinprofile_hash_algorithm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinprofile',
            name='open_source',
            field=models.BooleanField(null=True),
        ),
    ]
