# Generated by Django 4.2.4 on 2023-08-21 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 9, 43, 3, 245371, tzinfo=datetime.timezone.utc)),
        ),
    ]
