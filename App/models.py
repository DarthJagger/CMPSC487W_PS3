from django.db import models

# Create your models here.

class tenant(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_in = models.CharField(max_length=100)
    date_out = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)

    def __str__(self):
        return self.ID

class requests(models.Model):
    ID = models.AutoField(primary_key=True)
    apartment = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank = True )
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.ID



