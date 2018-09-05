from django.db import models


class Evnts(models.Model):
    title= models.CharField(max_length=300)
    details= models.CharField(max_length=850)
    address= models.CharField(max_length=300)
    source= models.CharField(max_length=500)
    dates= models.DateField()
    username= models.CharField(max_length=250)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.title





# Create your models here.
