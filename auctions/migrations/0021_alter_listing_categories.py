# Generated by Django 3.2.3 on 2021-05-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20210524_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(to='auctions.Category'),
        ),
    ]
