# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addr', models.CharField(default=b'', max_length=100)),
                ('reciever', models.CharField(default=b'', max_length=20)),
                ('phone', models.CharField(default=b'', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='useraddr',
            name='uname',
            field=models.ForeignKey(to='tt_user.UserInfo'),
        ),
    ]
