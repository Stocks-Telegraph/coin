# Generated by Django 4.1.2 on 2023-03-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_links', '0004_remove_explorerlinks_explorer_link_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_links',
        ),
        migrations.AddField(
            model_name='explorerlinks',
            name='explorer_link_1',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='explorerlinks',
            name='explorer_link_2',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='explorerlinks',
            name='explorer_link_3',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='explorerlinks',
            name='explorer_link_4',
            field=models.CharField(max_length=120, null=True),
        ),
    ]