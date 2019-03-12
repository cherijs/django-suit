# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-03-12 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0012_auto_20170407_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, 'Awesome'), (2, 'Good'), (3, 'Normal'), (4, 'Bad')], help_text='Choose wisely'),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(help_text='ISO 3166-1 alpha-2 - two character country code', max_length=2),
        ),
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, help_text='Try and enter few some more lines'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, 'Awesome'), (2, 'Good'), (3, 'Normal'), (4, 'Bad')], default=2),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='boolean_with_help',
            field=models.BooleanField(default=False, help_text='Boolean field with help text'),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='choices',
            field=models.SmallIntegerField(choices=[(1, 'Tall'), (2, 'Normal'), (3, 'Short')], default=3, help_text='Help text'),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='country2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showcase_country2_set', to='demo.Country', verbose_name='Django Select 2'),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='help_text',
            field=models.CharField(help_text='Enter fully qualified name', max_length=64),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='horizontal_choices',
            field=models.SmallIntegerField(choices=[(1, 'Awesome'), (2, 'Good'), (3, 'Normal'), (4, 'Bad')], default=1, help_text='Horizontal choices look like this'),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='multiple_in_row',
            field=models.CharField(help_text='Help text for multiple', max_length=64),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='readonly_field',
            field=models.CharField(default='Some value here', max_length=127),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='textfield',
            field=models.TextField(blank=True, help_text='Try and enter few some more lines', verbose_name='Autosized textfield'),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='time_only',
            field=models.TimeField(blank=True, null=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='vertical_choices',
            field=models.SmallIntegerField(choices=[(1, 'Hot'), (2, 'Normal'), (3, 'Cold')], default=2, help_text='Some help on vertical choices'),
        ),
    ]
