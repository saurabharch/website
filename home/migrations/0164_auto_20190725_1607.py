# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-25 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0163_auto_20190725_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roundpage',
            name='outreachy_chat',
            field=models.DateTimeField(verbose_name='Date and time of the Outreachy Twitter chat'),
        ),
    ]
