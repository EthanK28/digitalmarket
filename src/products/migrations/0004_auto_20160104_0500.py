# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=100, default=6.99, blank=True, null=True),
        ),
    ]
