# Generated by Django 4.1.2 on 2023-02-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_twitter_tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twittertweets',
            name='media_link',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='twittertweets',
            name='youtube_link',
            field=models.CharField(max_length=120, null=True),
        ),
    ]