from django.contrib import admin
from .models import Complainant, Complaint, Feedback, Appeal

# Register your models here.
admin.site.register(Complainant)
admin.site.register(Complaint)
admin.site.register(Feedback)
admin.site.register(Appeal)

# @admin.register(ComplaintsForm)
# class ComplaintsModel(admin.ModelAdmin):
# 	list_filter = ('Complain_description', 'date')
# 	list_display = ('Complain_description', 'date')

# @admin.register(RegistrationForm)
# class RegistrationModel(admin.ModelAdmin):
# 	list_filter = ('First_Name', 'Last_Name', 'RegNo')
# 	list_display = ('First_Name', 'Last_Name', 'RegNo')
