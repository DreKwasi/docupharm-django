from interventions.models import InterventionResponses, Interventions, Medications, Patients
from rest_framework import generics, mixins, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import InterventionResponsesSerializer, PatientsSerializer, InterventionsSerializer, MedicationsSerializer
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


class InterventionResponsesApiViewset(CreateListRetrieveViewSet):
    serializer_class = InterventionResponsesSerializer
    queryset = InterventionResponses.objects.all()


class MedicationsApiViewset(CreateListRetrieveViewSet):
    serializer_class = MedicationsSerializer
    queryset = Medications.objects.all()


class InterventionApiViewset(CreateListRetrieveViewSet):
    serializer_class = InterventionsSerializer
    queryset = Interventions.objects.all()


class PatientsApiViewset(CreateListRetrieveViewSet):
    serializer_class = PatientsSerializer
    queryset = Patients.objects.all()