from django.contrib import admin
from .models import ComplaintsForm

# Register your models here.
# admin.site.register(ComplaintsForm)

@admin.register(ComplaintsForm)
class ArticleModel(admin.ModelAdmin):
	list_filter = ('Complain_description', 'date')
	list_display = ('Complain_description', 'date')
