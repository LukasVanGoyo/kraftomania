# Generated by Django 4.2.4 on 2023-08-17 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='pkt',
        ),
    ]