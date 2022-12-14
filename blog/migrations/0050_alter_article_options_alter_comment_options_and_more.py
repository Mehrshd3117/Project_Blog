# Generated by Django 4.0.1 on 2022-07-11 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_alter_article_pub_date_alter_message_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created',), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقاله ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرها'},
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/articles', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 9, 9, 58, 74776, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=True, verbose_name='منتشر شده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='ادرس اینترنتی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=70, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 9, 9, 58, 77794, tzinfo=utc)),
        ),
    ]
