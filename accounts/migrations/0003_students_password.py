# Generated by Django 2.0.6 on 2018-09-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='password',
            field=models.IntegerField(blank=True, default=False),
        ),
    ]
