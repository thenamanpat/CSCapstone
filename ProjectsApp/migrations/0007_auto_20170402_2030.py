# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-02 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0010_auto_20170402_2030'),
        ('CSCapstoneApp', '__first__'),
        ('ProjectsApp', '0006_auto_20170306_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='languages',
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(related_name='project_set', to='CSCapstoneApp.SkillTag'),
        ),
        migrations.DeleteModel(
            name='ProgrammingLanguage',
        ),
    ]
