from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClinicalData(models.Model):
    componentName = models.CharField(
        choices=[
            ("BP", "Blood Pressure"),
            ("Sugar", "Sugar Level"),
            ("Hemoglobin", "Hemoglobin"),
        ]
    )
    componentValue = models.FloatField(default=0)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
