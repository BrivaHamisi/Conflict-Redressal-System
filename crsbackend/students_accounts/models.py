from operator import mod
from unittest import mock
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ComplaintsForm(models.Model):
    Complain_description = models.CharField(max_length=100, null=True)
    Events_that_took_Place = models.TextField(max_length=200, null=True)
    Consequence_suffered =models.TextField(max_length=200, null=True)
    Spoken_to_someone = models.TextField(max_length=200, null=True)
    Dissatisfied_with_Informal_complaint = models.TextField(max_length=200, null=True)
    evidence = models.TextField(max_length=200, null=True) 
    recommendation = models.TextField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status_of_complaint = models.TextField(max_length=25, null=True)

    def __str__(self):
        return self.Complain_description

class RegistrationForm(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    First_Name = models.CharField(max_length=100, null=True)
    Last_Name = models.CharField(max_length=100, null=True)

    RegNo = models.CharField(max_length=100, null=True)
    Course = models.CharField(max_length=100, null=True)
    Campus = models.CharField(max_length=100, null=True)
    Phone_Number = models.CharField(max_length=100, null=True)
    Email = models.CharField(max_length=100, null=True)
    Department = models.CharField(max_length=100, null=True)
    Password = models.CharField(max_length=100, null=True)
    Confirm_Password = models.CharField(max_length=100, null=True)

class FeedbackForm(models.Model):
    AppealId = models.CharField(null=True, max_length=50)
    ComplaintId = models.CharField(null = True, max_length=50)
    AdminId = models.CharField(null=True, max_length=50)
    Content = models.CharField(null=True, max_length=500)
    ActionTaken = models.CharField(null=True, max_length=500)
    Documents = models.CharField(null=True, max_length=50)


class AppealForm(models.Model):
    feebackId = models.CharField(null=True, max_length=50)
    Decision_Not_fair = models.CharField(null=True, max_length=500)
    What_To_Happen = models.CharField(null=True, max_length=500)



# class RegistrationForm(models.Model):
#     RegNo = models.CharField(max_length=100)
#     First_Name = models.CharField(max_length=100)
#     Last_Name = models.CharField(max_length=100)
#     Course = models.CharField(max_length=100)
#     Campus = models.CharField(max_length=100)
#     Phone_Number = models.CharField(max_length=100)
#     Email = models.CharField(max_length=100)
#     Department = models.CharField(max_length=100)
#     Password = models.CharField(max_length=100)
#     Confirm_Password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.RegNo



# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True,blank = True, on_delete=models.CASCADE)
#     name = models.CharField(max_length= 200, null=True)
#     phone = models.CharField(max_length= 200, null=True)
#     email = models.CharField(max_length= 200, null=True)
#     profile_pic = models.ImageField( default='default_profile.png',null=True, blank= True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)