# Generated by Django 2.2.6 on 2019-10-28 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]