# Generated by Django 4.0.1 on 2022-04-28 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 19, 12, 37, 379228, tzinfo=utc)),
        ),
    ]