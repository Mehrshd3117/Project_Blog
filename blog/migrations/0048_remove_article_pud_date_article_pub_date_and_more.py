# Generated by Django 4.0.1 on 2022-07-07 05:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_alter_article_pud_date_alter_message_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pud_date',
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 5, 24, 41, 793156, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 5, 24, 41, 801157, tzinfo=utc)),
        ),
    ]
