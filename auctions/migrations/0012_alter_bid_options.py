# Generated by Django 3.2.3 on 2021-05-20 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_rename_listing_id_bid_listing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ('-time',)},
        ),
    ]
