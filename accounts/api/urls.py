from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccountApiViewset, ProfileApiViewset

router = DefaultRouter()

router.register(r"all_accounts", AccountApiViewset, basename="accounts")
router.register(r"profiles", ProfileApiViewset, basename="profiles")

# router.register(r"facilities", FacilityApiViewset, basename="facilities")

urlpatterns = [path("/", include(router.urls))]
