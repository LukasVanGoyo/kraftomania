# Generated by Django 4.2.4 on 2023-08-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='votes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
