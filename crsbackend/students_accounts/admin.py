from django.contrib import admin
from .models import Complainant, Complaint, Feedback, Appeal
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Complainant)
# admin.site.register(Complaint)
admin.site.register(Feedback)
admin.site.register(Appeal)

@admin.register(Complaint)
class Complainant(ImportExportModelAdmin):
    pass
