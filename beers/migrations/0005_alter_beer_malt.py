# Generated by Django 4.1.7 on 2023-04-21 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_malt_style_brewery_country_brewery_year_beer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='malt',
            field=models.BinaryField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beers.malt')),
        ),
    ]
