# Generated by Django 4.0.1 on 2022-04-28 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_message_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MongoTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 19, 6, 7, 134682, tzinfo=utc)),
        ),
    ]