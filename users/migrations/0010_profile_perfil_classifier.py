# Generated by Django 3.1.5 on 2021-02-06 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_mostrar_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='perfil_classifier',
            field=models.IntegerField(default=0),
        ),
    ]
