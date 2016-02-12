# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_auto_20160120_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('height', models.CharField(max_length=20, null=True, blank=True)),
                ('width', models.CharField(max_length=20, null=True, blank=True)),
                ('media', models.ImageField(width_field='width', height_field='height', upload_to=products.models.download_mdedia_location, blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='c:\\dev\\django\\digitalmarket\\static_cdn\\protected'), null=True, upload_to=products.models.download_mdedia_location, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='managers',
            field=models.ManyToManyField(related_name='managers_product', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
