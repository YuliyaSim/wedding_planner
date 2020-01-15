# Generated by Django 3.0.2 on 2020-01-08 11:37

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('website', models.URLField(max_length=250)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('notes', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2020-01-08'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2020-01-08'),
        ),
    ]