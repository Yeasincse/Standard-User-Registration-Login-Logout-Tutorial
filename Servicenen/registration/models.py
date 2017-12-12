from django.db import models
from django.contrib.auth.models import User


class Division(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    city=models.ForeignKey(Division,on_delete=models.CASCADE)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    area=models.ForeignKey(Village,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()

    def __str__(self):
        return str(self.user)

