from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)



class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



class Device(models.Model):
    name = models.CharField(max_length=100)



class Asset(models.Model):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

