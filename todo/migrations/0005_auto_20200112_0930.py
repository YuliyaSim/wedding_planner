# Generated by Django 3.0.2 on 2020-01-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200108_1319'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coordination',
            new_name='Coordinator',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2020-01-12'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2020-01-12'),
        ),
    ]
