from rest_framework import serializers
from accounts.models import Account, Profile, Employer, Location


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = "__all__"
