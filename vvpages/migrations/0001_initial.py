# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 09:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsoneditor.fields.django_jsonfield
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_description', models.CharField(blank=True, help_text='Short description of the page content', max_length=256, null=True, verbose_name='SEO: description')),
                ('seo_keywords', models.CharField(blank=True, help_text='List of keywords separated by commas', max_length=120, null=True, verbose_name='SEO: keywords')),
                ('url', models.CharField(db_index=True, max_length=180, verbose_name='Url')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('edited', models.DateTimeField(auto_now=True, null=True, verbose_name='Edited')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('extra_data', jsoneditor.fields.django_jsonfield.JSONField(blank=True, default={}, verbose_name='Extra data')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('editor', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Edited by')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='vvpages.Page', verbose_name='Parent page')),
            ],
            options={
                'ordering': ['url'],
                'verbose_name': 'Page',
                'verbose_name_plural': 'Page',
            },
        ),
    ]