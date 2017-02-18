# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-18 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'feature',
            },
        ),
    ]