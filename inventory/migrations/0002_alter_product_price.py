# Generated by Django 5.0.1 on 2024-01-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.FloatField(),
        ),
    ]