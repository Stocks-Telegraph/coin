# Generated by Django 4.1.2 on 2023-03-17 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker_for_specific_coin', '0006_alter_tickerforspecificcoin_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickerforspecificcoin',
            name='volume_24h_change_24h',
        ),
    ]
