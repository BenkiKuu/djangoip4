# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyumba', '0005_allert_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='neighbourhoo_location',
            new_name='neighbourhood_location',
        ),
    ]
