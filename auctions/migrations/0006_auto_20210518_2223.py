# Generated by Django 3.2.3 on 2021-05-18 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210518_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listing',
        ),
        migrations.AddField(
            model_name='bid',
            name='listing_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
