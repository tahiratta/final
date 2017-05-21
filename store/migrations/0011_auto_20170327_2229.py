# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acadamic_record',
            name='id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='acadamic_record',
            name='a_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='g_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]