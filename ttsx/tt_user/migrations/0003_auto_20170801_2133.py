# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0002_auto_20170801_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='active_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default=b'', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
