# Generated by Django 4.1.2 on 2023-03-14 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0005_alter_performancechange_half_yearly_percentage_change_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performancechange',
            old_name='coin_profile',
            new_name='symbol',
        ),
    ]