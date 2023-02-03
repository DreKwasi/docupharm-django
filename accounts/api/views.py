from accounts.models import Account, Profile, Employer
from rest_framework import generics, mixins, status, viewsets
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AccountSerializer, ProfileSerializer, EmployerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
import pandas as pd
import numpy as np
from django.conf import settings
import os 
from django.http import HttpResponse


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


class EmployerApiViewset(CreateListRetrieveViewSet, mixins.DestroyModelMixin):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


# class LocationApiViewset(CreateListRetrieveViewSet, mixins.DestroyModelMixin):
#     serializer_class = LocationSerializer
#     queryset = Location.objects.all()
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             file = serializer.validated_data['file'] if 'file' in serializer.validated_data else None
            
#             if file:
#                 df = pd.read_csv(file)
#                 df = df.replace({np.nan:None})
#                 np_df = np.array(df)
#                 Location.objects.bulk_create( np_df)
#             else:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LocationCsvAPIView(views.APIView):
    parser_classes = [FileUploadParser,]
    
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, "locations.csv")
        file = pd.read_csv(file_path)
        output = file['Locations'].values.tolist()

        return Response(output)
    