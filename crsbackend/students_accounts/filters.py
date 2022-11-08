import django_filters

from . models import *


class ComplaintFilter(django_filters.FilterSet):
    class Meta:
        models = Complaint
        fields = '__all__'