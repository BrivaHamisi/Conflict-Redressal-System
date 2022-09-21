from rest_framework import serializers 
from .models import ComplaintsForm
from django.contrib.auth.models import User

class ComplaintsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintsForm
        fields = ('id','Complain_description', 'Events_that_took_Place', 'Consequence_suffered', 'Spoken_to_someone','Dissatisfied_with_Informal_complaint','evidence', 'recommendation', 'date', 'status_of_complaint')