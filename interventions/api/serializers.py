from interventions.models import Intervention, Patient
from accounts.models import Account
from rest_framework import serializers


class InterventionSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        "patient_name", queryset=Patient.objects.all(), required=True
    )
    user = serializers.SlugRelatedField(
        "username", queryset=Account.objects.all(), required=True
    )

    class Meta:
        model = Intervention
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=Account.objects.all(),
        required=False
    )

    class Meta:
        model = Patient
        fields = "__all__"
