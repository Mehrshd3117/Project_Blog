# Generated by Django 4.0.1 on 2022-06-15 12:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_remove_article_pub_date_alter_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 12, 16, 0, 283531, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 12, 16, 0, 284532, tzinfo=utc)),
        ),
    ]
