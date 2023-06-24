from django.contrib import admin
from .models import Intervention, Patient


class InterventionAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "pharmaceutical_care",
        "pharmaceutical_details",
        "medication",
        "proposed_intervention",
        "details",
    )
    ordering = (
        "-created_date",
    )

admin.site.register(Intervention, InterventionAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "age",
        "gender",
    )
    ordering = (
        "-created_date",
    )

admin.site.register(Patient, PatientAdmin)