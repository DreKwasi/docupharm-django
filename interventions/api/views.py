from interventions.models import Interventions, Patients
from rest_framework import generics, mixins, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PatientsSerializer, InterventionsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response


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


class InterventionApiViewset(CreateListRetrieveViewSet):
    serializer_class = InterventionsSerializer
    queryset = Interventions.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient = Patients.objects.create(gender="Male")
            patient.save()
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class PatientsApiViewset(CreateListRetrieveViewSet):
    serializer_class = PatientsSerializer
    queryset = Patients.objects.all()