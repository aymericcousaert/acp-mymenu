# Generated by Django 2.2.6 on 2019-10-27 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_todaysmenudish'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodaysMenuDish',
            new_name='DailySpecial',
        ),
    ]