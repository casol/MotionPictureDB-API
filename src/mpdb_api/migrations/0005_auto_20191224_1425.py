# Generated by Django 2.2.9 on 2019-12-24 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mpdb_api', '0004_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='added',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='favorite',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favorite',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]