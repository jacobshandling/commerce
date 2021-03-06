# Generated by Django 3.2.3 on 2021-05-21 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210520_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingcomment',
            name='listing',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listingcomment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listingcomment',
            name='content',
            field=models.TextField(max_length=2200),
        ),
        migrations.AlterField(
            model_name='listingcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
