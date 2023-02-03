from rest_framework import serializers
from accounts.models import Account, Profile, Employer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"


class EmployerSerializer(serializers.ModelSerializer):
    profile = serializers.SlugRelatedField(slug_field="account",
                                           queryset=Profile.objects.all(),
                                           required=False)

    class Meta:
        model = Employer
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"

