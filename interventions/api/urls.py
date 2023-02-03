from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (InterventionApiViewset, PatientsApiViewset)

router = DefaultRouter()

router.register(r"all_interventions",
                InterventionApiViewset,
                basename="all_interventions")

router.register(r"all_patients", PatientsApiViewset, basename="all_patients")

urlpatterns = [path("/", include(router.urls))]
