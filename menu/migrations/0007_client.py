# Generated by Django 2.2.6 on 2019-10-31 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20191028_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Mail')),
                ('token', models.CharField(default=None, max_length=20, verbose_name='token')),
            ],
        ),
    ]
