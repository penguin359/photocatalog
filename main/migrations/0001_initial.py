# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('comment', models.CharField(default=b'', max_length=30)),
                ('description', models.CharField(default=b'', max_length=30)),
                ('kind', models.CharField(default=b'', max_length=30)),
            ],
        ),
    ]
