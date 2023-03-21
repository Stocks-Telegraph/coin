# Generated by Django 4.1.2 on 2023-03-21 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coin_profile', '0011_alter_coinprofile_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('adj_close', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('unadjusted_volume', models.BigIntegerField()),
                ('change', models.FloatField()),
                ('change_percent', models.FloatField()),
                ('vwap', models.FloatField()),
                ('change_over_time', models.FloatField()),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin_profile.coinprofile')),
            ],
            options={
                'verbose_name_plural': 'Crypto Historical Data',
            },
        ),
    ]
