# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180510_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default=b'books/empty_cover.jpg', upload_to=store.models.cover_upload_path),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 14, 7, 33, 15, 500000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 14, 7, 33, 15, 500000, tzinfo=utc)),
        ),
    ]
