# Generated by Django 4.1.2 on 2023-03-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0003_performancechange_half_yearly_percentage_change_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancechange',
            name='year_to_date',
            field=models.IntegerField(null=True),
        ),
    ]
