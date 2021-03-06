# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acadamic_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_id', models.CharField(max_length=40)),
                ('attendance', models.CharField(max_length=40)),
                ('quiz_number', models.IntegerField(default=0)),
                ('quiz_marks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_id', models.CharField(max_length=40)),
                ('status', models.TextField(default='', max_length=50)),
                ('files', models.FileField(max_length=500, upload_to='')),
                ('comments', models.TextField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=40)),
                ('status', models.TextField(default='', max_length=50)),
                ('files', models.FileField(max_length=500, upload_to='')),
                ('comments', models.TextField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(blank=True, default='0', max_length=40, null=True)),
                ('name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('cell_number', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=40)),
                ('date_of_birth', models.DateField(max_length=40)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='post',
            name='u_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.User'),
        ),
        migrations.AddField(
            model_name='group',
            name='u_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.User'),
        ),
        migrations.AddField(
            model_name='acadamic_record',
            name='u_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.User'),
        ),
    ]
