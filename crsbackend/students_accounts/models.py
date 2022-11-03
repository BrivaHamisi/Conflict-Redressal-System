from django.db import models
from django.contrib.auth.models import User
from students_accounts.signals import receiver, post_save # DO NOT REMOVE

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

COLOR_CHOICES = (
    ('submitted','SUBMITTED'),
    ('pending', 'PENDING'),
    ('solved','SOLVED'),
    ('appealed','APPEALED'),
)


class Complainant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    campus = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    


class Complaint(models.Model):
    user = models.ForeignKey(Complainant, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.CharField(max_length=100, null=True)
    events_that_took_place = models.TextField(max_length=200, null=True)
    consequence_suffered =models.TextField(max_length=200, null=True)
    spoken_to_someone = models.TextField(max_length=200, null=True)
    dissatisfied_with_informal_complaint = models.TextField(max_length=200, null=True)
    evidence = models.TextField(max_length=200, null=True) 
    recommendation = models.TextField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status_of_complaint = models.CharField(max_length=25,choices=COLOR_CHOICES, default='submitted', null=True)

    def __str__(self):
        return f"{self.description}"


class Feedback(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.DO_NOTHING, null=True)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    content = models.CharField(null=True, max_length=500)
    action_taken = models.CharField(null=True, max_length=500)
    documents = models.CharField(null=True, max_length=50)
    feedback_status = models.CharField(null=True, max_length=50)


class Appeal(models.Model):
    user = models.ForeignKey(Complainant, on_delete=models.DO_NOTHING)
    feedback = models.OneToOneField(Feedback, on_delete=models.DO_NOTHING)
    decision_not_fair = models.CharField(null=True, max_length=500)
    what_to_happen = models.CharField(null=True, max_length=500)
    documents = models.CharField(null=True, max_length=50)


class GeneralIssuesUpdate(models.Model):
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    title = models.CharField(null=True, max_length=100)
    content = models.CharField(null=True, max_length=500)
    attached_documents = models.FileField(upload_to=None, max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="KU Conflict Redressal System"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
