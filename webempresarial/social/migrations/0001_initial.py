# Generated by Django 3.1.6 on 2021-02-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Nombre clave')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enclace')),
            ],
        ),
    ]