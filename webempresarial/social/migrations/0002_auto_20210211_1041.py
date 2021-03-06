# Generated by Django 3.1.6 on 2021-02-11 15:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'Enlace', 'verbose_name_plural': 'Enlaces'},
        ),
        migrations.AddField(
            model_name='link',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 11, 15, 41, 29, 577820, tzinfo=utc), verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Red social'),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace'),
        ),
    ]
