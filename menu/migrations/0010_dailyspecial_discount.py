# Generated by Django 2.2.6 on 2019-11-04 23:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20191103_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyspecial',
            name='discount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)], verbose_name='Porcentaje de Descuento'),
        ),
    ]
