# Generated by Django 4.1.2 on 2023-03-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_profile', '0010_alter_coinprofile_proof_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinprofile',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
