# Generated by Django 3.1.2 on 2020-10-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urban_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
