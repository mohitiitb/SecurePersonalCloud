from django.db import models

# Create your models here.

class registered_clients(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    class Meta:
        db_table = 'registered_clients'

class global_data(models.Model):
    user = models.ForeignKey('registered_clients',on_delete=models.CASCADE)
    file = models.BinaryField(max_length=1000)
    fname = models.CharField(max_length=100)
    ftype = models.CharField(max_length=50)
    fpath = models.CharField(max_length=100)

    class Meta:
        db_table = 'global_data'
