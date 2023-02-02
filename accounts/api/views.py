from accounts.models import Account, Profile, Employer
from rest_framework import generics, mixins, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AccountSerializer, ProfileSerializer, EmployerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


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
    authentication_classes = [BasicAuthentication]


class ProfileApiViewset(CreateListRetrieveViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class EmployerApiViewset(CreateListRetrieveViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()