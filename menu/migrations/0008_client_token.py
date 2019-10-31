
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='token',
            field=models.CharField(max_length=20, null=True)
        )
    ]
