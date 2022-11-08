from django.contrib import admin
from .models import Complainant, Complaint, Feedback, Appeal, GeneralIssuesUpdate
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Complainant)
# admin.site.register(Complaint)
# admin.site.register(Feedback)
# admin.site.register(Appeal)


@admin.register(Complaint)
class Complaint(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("user", "description", "date", "status_of_complaint")
    pass

@admin.register(Complainant)
class Complainant(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("user", "reg_no", "course", "campus", "phone_number", "department")
    pass

@admin.register(Appeal)
class Appeal(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("user", "feedback", "decision_not_fair", "what_to_happen", "documents")
    pass

@admin.register(Feedback)
class Feedback(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("complaint", "admin", "content", "action_taken", "documents", "feedback_status")
    pass

@admin.register(GeneralIssuesUpdate)
class GeneralIssuesUpdate(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("admin", "title", "content", "attached_documents", "date")
    pass
