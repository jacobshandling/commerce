# Generated by Django 3.2.3 on 2021-05-20 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_user_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='current_bid',
            new_name='current_price',
        ),
    ]
