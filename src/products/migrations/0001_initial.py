# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models
from django.conf import settings
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'verbose_name_plural': 'My Products',
                'verbose_name': 'My Products',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('media', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/es-mac/dev/django/dm/static_cdn/protected'), upload_to=products.models.download_mdedia_location)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=65, default=9.99, decimal_places=2)),
                ('sale_price', models.DecimalField(max_digits=65, blank=True, null=True, default=6.99, decimal_places=2)),
                ('managers', models.ManyToManyField(related_name='managers_product', blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('height', models.CharField(blank=True, null=True, max_length=20)),
                ('width', models.CharField(blank=True, null=True, max_length=20)),
                ('media', models.ImageField(blank=True, null=True, height_field='height', width_field='width', upload_to=products.models.download_mdedia_location)),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='myproducts',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.AddField(
            model_name='myproducts',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
