# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0004_auto_20170117_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='UniversitiesApp.Course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(to='UniversitiesApp.Course'),
        ),
    ]