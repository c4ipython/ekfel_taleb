# Generated by Django 2.0.6 on 2018-10-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20181023_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='salary',
            field=models.IntegerField(),
        ),
    ]