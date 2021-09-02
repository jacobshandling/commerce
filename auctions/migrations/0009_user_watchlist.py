# Generated by Django 3.2.3 on 2021-05-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_starting_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchers', to='auctions.Listing'),
        ),
    ]