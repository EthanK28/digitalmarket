# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160216_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/es-mac/dev/django/dm/static_cdn/protected'), upload_to=products.models.download_mdedia_location, blank=True),
        ),
    ]
