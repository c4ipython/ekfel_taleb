from django.db import models

# Create your models here.
class Req_st(models.Model):
    title=models.CharField(max_length=200)
    info=models.TextField(max_length=1900)
    sender=models.CharField(max_length=200)
    date_up=models.DateField(auto_now_add=True)
    sponser=models.CharField(max_length=200,blank=True)
    approved=models.BooleanField(default=False)
    req_spon=models.CharField(max_length=250,blank=True)
    disable=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Authentication (models.Model):
    types=[
        ('manger','manger'),
        ('student', 'student'),
        ('sponser', 'sponser'),


    ]

    user_type=models.CharField(max_length=200,choices=types)
    def __str__(self):
        return self.user.username
