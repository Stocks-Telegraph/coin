# Generated by Django 4.1.2 on 2023-03-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_links', '0010_remove_explorerlinks_explorer_link_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explorerlinks',
            name='explorer_link',
            field=models.CharField(max_length=1020, null=True),
        ),
    ]