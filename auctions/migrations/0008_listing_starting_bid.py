# Generated by Django 3.2.3 on 2021-05-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210518_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='starting_bid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
