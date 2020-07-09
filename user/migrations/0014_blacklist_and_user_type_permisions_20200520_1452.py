# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_user_types_20200321_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('motive_of_ban', models.CharField(blank=True, max_length=300, null=True)),
                ('date_of_ban', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='can_review_blacklist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='can_review_mentors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='can_review_sponsors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='can_review_volunteers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='max_applications',
            field=models.IntegerField(default=1),
        ),
    ]
