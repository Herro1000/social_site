# Generated by Django 4.0.5 on 2022-06-13 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
