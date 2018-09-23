# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='player_one_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player_one_email',
            field=models.CharField(default='No Email Provided', max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='player_one_hall',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player_two_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='player_two_email',
            field=models.CharField(default='No Email Provided', max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='player_two_hall',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]