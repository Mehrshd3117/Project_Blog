# Generated by Django 4.0.1 on 2022-06-27 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'حساب کاربری', 'verbose_name_plural': 'حساب های کاربری'},
        ),
    ]
