# Generated by Django 2.0.6 on 2018-09-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180924_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
