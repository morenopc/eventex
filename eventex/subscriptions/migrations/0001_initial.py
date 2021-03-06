# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import eventex.subscriptions.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, validators=[eventex.subscriptions.validators.validate_cpf], verbose_name='CPF')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='telefone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('paid', models.BooleanField(default=False, verbose_name='pago')),
            ],
            options={
                'verbose_name_plural': 'inscrições',
                'ordering': ('-created_at',),
                'verbose_name': 'inscrição',
            },
        ),
    ]
