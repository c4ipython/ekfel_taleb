from django.db import models


# Create your models here.


class Sponsor(models.Model):
    username = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True)
    number = models.CharField(max_length=12, blank=False)
    city = models.CharField(max_length=50, blank=True)
    img = models.FileField(upload_to='docs/', blank=False)
    work = models.CharField(max_length=100, blank=False)
    work_locations = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=False)
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
    number = models.CharField(max_length=12, blank=False)
    city = models.CharField(max_length=50, blank=True)
    img = models.FileField(upload_to='docs/', blank=False)
    stage = models.CharField(max_length=50, blank=True)
    approved = models.BooleanField(default=False)
    up_date = models.DateField(auto_now_add=True)
    type_user = models.CharField(max_length=50, default='student')
    disabled = models.CharField(max_length=50, default=False)
    password = models.CharField(blank=False, default='', max_length=20)

    def __str__(self):

        return self.full_name

