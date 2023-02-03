from interventions.models import Interventions, Patients
from rest_framework import serializers

class InterventionsSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField("name",
                                           queryset=Patients.objects.all(),
                                           required=True)

    class Meta:
        model = Interventions
        fields = "__all__"


class PatientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patients
        fields = "__all__"
