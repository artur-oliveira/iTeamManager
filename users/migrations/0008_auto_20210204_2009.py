# Generated by Django 3.1.5 on 2021-02-04 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_secret_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='secret_hash',
            field=models.CharField(editable=False, max_length=30, unique=True),
        ),
    ]