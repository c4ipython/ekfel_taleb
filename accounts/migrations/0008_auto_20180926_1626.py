# Generated by Django 2.0.6 on 2018-09-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180926_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='city',
            field=models.CharField(blank=True, choices=[('Baghdad', 'Baghdad'), ('Karbala', 'Karbala'), ('Deyala', 'Deyala'), ('basrah', 'basrah')], max_length=50),
        ),
    ]
