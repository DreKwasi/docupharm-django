from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (InterventionApiViewset, PatientsApiViewset,
                    PharmaCareApiView, DetailCareApiView, SolutionApiView)

router = DefaultRouter()

router.register(r"all_interventions",
                InterventionApiViewset,
                basename="all_interventions")

router.register(r"all_patients", PatientsApiViewset, basename="all_patients")

urlpatterns = [
    path("pharma_care/", PharmaCareApiView.as_view()),
    path("detailed_care/<str:pharma_care>/", DetailCareApiView.as_view()),
    path("solution/<str:pharma_care>/", SolutionApiView.as_view()),
    path("", include(router.urls))
]
