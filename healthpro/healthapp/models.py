from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.name


class Mayo_doct(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Patients(models.Model):
    name = models.CharField(max_length=100)

class PatientFullDetails():

    def __str__(self):
        return self.name

