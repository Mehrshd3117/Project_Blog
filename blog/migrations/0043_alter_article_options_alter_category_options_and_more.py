# Generated by Django 4.0.1 on 2022-06-27 12:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0042_article_pud_date_alter_message_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created',), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده ی مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='artilces', to='blog.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pud_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 12, 3, 55, 845235, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 12, 3, 55, 846235, tzinfo=utc)),
        ),
    ]