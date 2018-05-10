# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180507_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default=b'books/empty_cover.jpg', upload_to=b'books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 10, 6, 15, 56, 742000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 10, 6, 15, 56, 742000, tzinfo=utc)),
        ),
    ]
