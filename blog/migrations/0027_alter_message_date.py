# Generated by Django 4.0.1 on 2022-04-28 18:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_message_age_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 18, 58, 4, 936410, tzinfo=utc)),
        ),
    ]
