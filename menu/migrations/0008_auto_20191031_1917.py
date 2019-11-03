# Generated by Django 2.2.6 on 2019-10-31 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='token',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='token'),
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='description')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Client')),
            ],
        ),
    ]
