# Generated by Django 4.1.2 on 2023-02-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterTweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(max_length=120)),
                ('user_image_link', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
                ('is_retweet', models.BooleanField()),
                ('retweet_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('status_id', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Twitter Tweets',
            },
        ),
    ]
