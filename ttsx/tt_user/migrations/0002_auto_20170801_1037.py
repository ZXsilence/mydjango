# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='useraddr',
            table='useraddr',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='userinfo',
        ),
    ]
