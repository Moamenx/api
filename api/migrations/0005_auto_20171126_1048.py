# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=1)),
                ('register_date', models.IntegerField()),
                ('current_ip', models.CharField(max_length=45)),
                ('register_ip', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('setting_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Setting')),
            ],
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
