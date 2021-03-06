from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

LIST_STUDENT =(
    ('الانبار', 'الانبار'),
    ('البصره', 'البصره'),
    ('المثنى', 'المثنى'),
    ('القادسيه', 'القادسيه'),
    ('النجف', 'النجف'),
    ('اربيل', 'اربيل'),
    ('سليمانية', 'سليمانية'),
    ('بابل', 'بابل'),
    ('بغداد', 'بغداد'),
    ('دهوك', 'دهوك'),
    ('ذي قار', 'ذي قار'),
    ('ديالى', 'ديالى'),
    ('كربلاء', 'كربلاء'),
    ('كركوك', 'كركوك'),
    ('ميسان', 'ميسان'),
    ('نينوى', 'نينوى'),
    ('صلاح الدين', 'صلاح الدين'),
    ('واسط', 'واسط'),
)

list_stage = (
        ('اول ابتدائي', 'اول ابتدائي'),
        ('ثاني ابتدائي', 'ثاني ابتدائي'),
        ('ثالث ابتدائي', 'ثالث ابتدائي'),
        ('رابع ابتدائي', 'رابع ابتدائي'),
        ('خامس ابتدائي', 'خامس ابتدائي'),
        ('سادس ابتدائي', 'سادس ابتدائي'),
        ('اول متوسط', 'اول متوسط'),
        ('ثاني متوسط', 'ثاني متوسط'),
        ('ثالث متوسط', 'ثالث متوسط'),
        ('رابع اعدادي', 'رابع اعدادي'),
        ('خامس اعدادي', 'خامس اعدادي'),
        ('سادس اعدادي', 'سادس اعدادي'),
)

PROVINCE_LIST =(
    ('الانبار', 'الانبار'),
    ('البصره', 'البصره'),
    ('المثنى', 'المثنى'),
    ('القادسيه', 'القادسيه'),
    ('النجف', 'النجف'),
    ('اربيل', 'اربيل'),
    ('سليمانية', 'سليمانية'),
    ('بابل', 'بابل'),
    ('بغداد', 'بغداد'),
    ('دهوك', 'دهوك'),
    ('ذي قار', 'ذي قار'),
    ('ديالى', 'ديالى'),
    ('كربلاء', 'كربلاء'),
    ('كركوك', 'كركوك'),
    ('ميسان', 'ميسان'),
    ('نينوى', 'نينوى'),
    ('صلاح الدين', 'صلاح الدين'),
    ('واسط', 'واسط'),
)


class Sponsor(models.Model):
    username = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True)
    phone_number = PhoneNumberField(blank=False, default='', help_text="use +9647700000000")
    city = models.CharField(max_length=50, blank=True, choices=PROVINCE_LIST)
    img = models.FileField(upload_to='docs/', blank=False)
    work = models.CharField(max_length=100, blank=False)
    work_locations = models.CharField(max_length=100, blank=True)
    salary = models.IntegerField(blank=False)
    approved = models.BooleanField(default=False)
    up_date = models.DateField(auto_now_add=True)
    type_user = models.CharField(max_length=50, default='sponsor')
    disabled = models.CharField(max_length=50, default=False)
    password = models.CharField(blank=False, default='', max_length=20)

    def __str__(self):

        return self.full_name


class Students(models.Model):
    username = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True)
    phone_number = PhoneNumberField(blank=False, default='', help_text="use +9647700000000")
    city = models.CharField(max_length=50, choices=LIST_STUDENT)
    img = models.FileField(upload_to='docs/', blank=False)
    stage = models.CharField(max_length=50, choices=list_stage)
    approved = models.BooleanField(default=False)
    up_date = models.DateField(auto_now_add=True)
    type_user = models.CharField(max_length=50, default='student')
    disabled = models.CharField(max_length=50, default=False)
    password = models.CharField(blank=False, default='', max_length=20)

    def __str__(self):

        return self.full_name

