# Generated by Django 3.1.5 on 2021-02-04 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20210203_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='share_hash',
            field=models.CharField(editable=False, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='url_hash',
            field=models.CharField(editable=False, max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='UsuarioRecusado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visualizou', models.BooleanField(default=False)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projeto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='projeto',
            name='recusados',
            field=models.ManyToManyField(blank=True, related_name='usuarios_recusados', through='app.UsuarioRecusado', to=settings.AUTH_USER_MODEL),
        ),
    ]
