# Generated by Django 2.0.6 on 2018-10-23 17:40

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180926_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='city',
            field=models.CharField(blank=True, choices=[('الانبار', 'الانبار'), ('البصره', 'البصره'), ('المثنى', 'المثنى'), ('القادسيه', 'القادسيه'), ('النجف', 'النجف'), ('اربيل', 'اربيل'), ('سليمانية', 'سليمانية'), ('بابل', 'بابل'), ('بغداد', 'بغداد'), ('دهوك', 'دهوك'), ('ذي قار', 'ذي قار'), ('ديالى', 'ديالى'), ('كربلاء', 'كربلاء'), ('كركوك', 'كركوك'), ('ميسان', 'ميسان'), ('نينوى', 'نينوى'), ('صلاح الدين', 'صلاح الدين'), ('واسط', 'واسط')], max_length=50),
        ),
        migrations.AlterField(
            model_name='students',
            name='city',
            field=models.CharField(choices=[('الانبار', 'الانبار'), ('البصره', 'البصره'), ('المثنى', 'المثنى'), ('القادسيه', 'القادسيه'), ('النجف', 'النجف'), ('اربيل', 'اربيل'), ('سليمانية', 'سليمانية'), ('بابل', 'بابل'), ('بغداد', 'بغداد'), ('دهوك', 'دهوك'), ('ذي قار', 'ذي قار'), ('ديالى', 'ديالى'), ('كربلاء', 'كربلاء'), ('كركوك', 'كركوك'), ('ميسان', 'ميسان'), ('نينوى', 'نينوى'), ('صلاح الدين', 'صلاح الدين'), ('واسط', 'واسط')], max_length=50),
        ),
        migrations.AlterField(
            model_name='students',
            name='stage',
            field=models.CharField(choices=[('اول ابتدائي', 'اول ابتدائي'), ('ثاني ابتدائي', 'ثاني ابتدائي'), ('ثالث ابتدائي', 'ثالث ابتدائي'), ('رابع ابتدائي', 'رابع ابتدائي'), ('خامس ابتدائي', 'خامس ابتدائي'), ('سادس ابتدائي', 'سادس ابتدائي'), ('اول متوسط', 'اول متوسط'), ('ثاني متوسط', 'ثاني متوسط'), ('ثالث متوسط', 'ثالث متوسط'), ('رابع اعدادي', 'رابع اعدادي'), ('خامس اعدادي', 'خامس اعدادي'), ('سادس اعدادي', 'سادس اعدادي')], max_length=50),
        ),
    ]
