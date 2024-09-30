# Generated by Django 5.1.1 on 2024-09-30 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_alter_product_category_alter_product_seller'),
        ('suborders', '0002_rename_suborden_suborder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuborderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('sold_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suborder_product', to='products.product')),
                ('suborder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suborder_product', to='suborders.suborder')),
            ],
        ),
    ]
