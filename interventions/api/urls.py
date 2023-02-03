from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (InterventionResponsesApiViewset, MedicationsApiViewset,
                    InterventionApiViewset, PatientsApiViewset)

router = DefaultRouter()
router.register(r"intervention_responses",
                InterventionResponsesApiViewset,
                basename="intervention_responses")

router.register(r"medications",
                MedicationsApiViewset,
                basename="medications")

router.register(r"interventions",
                InterventionApiViewset,
                basename="interventions")

router.register(r"patients",
                PatientsApiViewset,
                basename="patients")

urlpatterns = [path("/", include(router.urls))]
