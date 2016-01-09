# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=64)),
                ('ip', models.CharField(max_length=64)),
                ('device', models.CharField(max_length=64)),
                ('time_out', models.DateTimeField(max_length=64)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=16)),
                ('sex', models.IntegerField(default=0)),
                ('password_salt', models.CharField(max_length=16)),
                ('password_encryption', models.CharField(max_length=64)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('is_user_enable', models.BooleanField(default=True)),
                ('email_verification_code', models.CharField(max_length=32)),
                ('phone_verification_code', models.CharField(max_length=32)),
                ('reset_password_code', models.CharField(max_length=32)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='loginhistory',
            name='uid',
            field=models.ForeignKey(to='db.User'),
        ),
    ]
