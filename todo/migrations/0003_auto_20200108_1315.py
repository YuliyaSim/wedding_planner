# Generated by Django 3.0.2 on 2020-01-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200108_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordination',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
