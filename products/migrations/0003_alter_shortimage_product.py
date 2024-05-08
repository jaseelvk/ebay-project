# Generated by Django 5.0.4 on 2024-05-02 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='short_images', to='products.product'),
        ),
    ]