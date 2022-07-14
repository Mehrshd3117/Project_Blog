# Generated by Django 4.0.1 on 2022-07-11 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0050_alter_article_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 9, 13, 2, 116233, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 9, 13, 2, 118249, tzinfo=utc)),
        ),
    ]