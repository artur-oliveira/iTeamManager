# Generated by Django 3.1.5 on 2021-02-03 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210203_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='share_hash',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='url_hash',
            field=models.CharField(editable=False, max_length=10, unique=True),
        ),
    ]
