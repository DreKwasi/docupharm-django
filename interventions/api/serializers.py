from interventions.models import InterventionResponses, Medications, Interventions, Patients
from rest_framework import serializers


class InterventionResponsesSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterventionResponses
        fields = "__all__"


class MedicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medications
        fields = "__all__"


class InterventionsSerializer(serializers.ModelSerializer):
    patients = serializers.SlugRelatedField("name",
                                            queryset=Patients.objects.all(),
                                            required=False)

    class Meta:
        model = Interventions
        fields = "__all__"


class PatientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patients
        fields = "__all__"
