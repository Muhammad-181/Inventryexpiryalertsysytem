# Generated by Django 5.0.1 on 2024-01-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_product_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]