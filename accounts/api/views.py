from accounts.models import Account, Profile
from rest_framework import generics, mixins, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AccountSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated


class CreateListRetrieveViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass


class AccountApiViewset(CreateListRetrieveViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]


class ProfileApiViewset(CreateListRetrieveViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()