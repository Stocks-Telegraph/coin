# Generated by Django 4.1.2 on 2023-02-21 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin_twitter_tweets', '0002_twittertweets_media_link_twittertweets_youtube_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twittertweets',
            name='media_link',
        ),
        migrations.RemoveField(
            model_name='twittertweets',
            name='youtube_link',
        ),
    ]