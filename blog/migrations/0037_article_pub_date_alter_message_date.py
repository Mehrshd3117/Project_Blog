# Generated by Django 4.0.1 on 2022-06-14 19:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_delete_mongotest_alter_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 19, 32, 48, 660977, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 19, 32, 48, 661977, tzinfo=utc)),
        ),
    ]
