# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-02 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0015_group_group_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_skills',
        ),
    ]
