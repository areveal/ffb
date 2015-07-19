# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nflgame_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('college', models.CharField(max_length=50, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('height', models.IntegerField(default=0, null=True, blank=True)),
                ('weight', models.IntegerField(default=0, null=True, blank=True)),
                ('position', models.CharField(max_length=50, null=True, blank=True)),
                ('team', models.CharField(max_length=4, null=True, blank=True)),
            ],
        ),
    ]
