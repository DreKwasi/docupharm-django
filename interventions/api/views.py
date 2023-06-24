from interventions.models import Intervention, Patient
from rest_framework import generics, mixins, status, viewsets, views
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PatientSerializer, InterventionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from django.conf import settings
import os, json
import jwt
from accounts.models import Account


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


def get_user_details(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    token = str.replace(str(token), "Bearer ", "")
    try:
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
        user = Account.objects.get(id=payload["user_id"])
    except jwt.ExpiredSignatureError as e:
        return Response(
            {"error": "Activations link expired"}, status=status.HTTP_400_BAD_REQUEST
        )
    except jwt.DecodeError as e:
        return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
    return user


class InterventionApiViewset(CreateListRetrieveViewSet):
    serializer_class = InterventionSerializer
    queryset = Intervention.objects.all()
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient = Patient.objects.create(gender="Male")
            patient.save()
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = get_user_details(request)
        print(user)
        queryset = Intervention.objects.filter(user=user)
        serializer = InterventionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatientsApiViewset(CreateListRetrieveViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = get_user_details(request)
        print(user)
        queryset = Patient.objects.filter(user=user)
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = get_user_details(request)
        serializer_data = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer_data.is_valid():
            serializer_data.save(user=user)
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response(
            {"error": serializer_data.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class PharmaCareApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, "interventions.json")
        with open(file_path, "r") as f:
            interventions = json.load(f)

        output = interventions.keys()
        return Response(output, status=status.HTTP_200_OK)


class DetailCareApiView(views.APIView):
    def get(self, request, pharma_care, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, "interventions.json")
        with open(file_path, "r") as f:
            interventions = json.load(f)

        output = interventions[pharma_care]["reason"]
        return Response(output, status=status.HTTP_200_OK)


class SolutionApiView(views.APIView):
    def get(self, request, pharma_care, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, "interventions.json")
        with open(file_path, "r") as f:
            interventions = json.load(f)

        output = interventions[pharma_care]["solution"]
        return Response(output, status=status.HTTP_200_OK)
