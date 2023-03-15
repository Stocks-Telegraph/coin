# Generated by Django 4.1.2 on 2023-03-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_links', '0005_remove_explorerlinks_explorer_links_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_1',
        ),
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_2',
        ),
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_3',
        ),
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_4',
        ),
        migrations.AddField(
            model_name='explorerlinks',
            name='explorer_links',
            field=models.URLField(default=None),
        ),
    ]