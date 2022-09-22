from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ComplaintsForm(models.Model):
    Complain_description = models.CharField(max_length=100)
    Events_that_took_Place = models.TextField()
    Consequence_suffered =models.TextField()
    Spoken_to_someone = models.TextField()
    Dissatisfied_with_Informal_complaint = models.TextField()
    evidence = models.TextField() 
    recommendation = models.TextField()
    date = models.TextField()
    status_of_complaint = models.TextField()

    def __str__(self):
        return self.Complain_description

class RegistrationForm(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)

    RegNo = models.CharField(max_length=100)
    Course = models.CharField(max_length=100)
    Campus = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100)


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