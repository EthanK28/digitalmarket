# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='managers',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, related_name='product_managers'),
            preserve_default=False,
        ),
    ]
