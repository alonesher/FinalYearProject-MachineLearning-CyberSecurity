from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address= models.CharField(max_length=3000)
    gender= models.CharField(max_length=30)

class cyber_attack_detection_type(models.Model):

    idnumber= models.CharField(max_length=3000)
    datetime= models.CharField(max_length=3000)
    host= models.CharField(max_length=3000)
    RID= models.CharField(max_length=3000)
    proto= models.CharField(max_length=3000)
    spt= models.CharField(max_length=3000)
    dtp= models.CharField(max_length=3000)
    ipaddress= models.CharField(max_length=3000)
    cc= models.CharField(max_length=3000)
    country= models.CharField(max_length=3000)
    locale= models.CharField(max_length=3000)
    latitude= models.CharField(max_length=3000)
    longitude= models.CharField(max_length=3000)
    Sources= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



