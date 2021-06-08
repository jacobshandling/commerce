# Generated by Django 3.2.3 on 2021-05-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210522_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='listings',
        ),
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(related_name='listings', to='auctions.Category'),
        ),
    ]
