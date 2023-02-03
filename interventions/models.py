from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Patients(models.Model):
    name = models.CharField(max_length=225)
    age = models.IntegerField()
    weight = models.IntegerField()
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message=
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=17,
                                    blank=True)
    further_details = models.TextField(blank=True, max_length=225, null=True)


class Interventions(models.Model):
    user = models.ForeignKey("accounts.account",
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name="accounts_interventions")
    patient = models.ForeignKey(Patients, null=True, on_delete=models.SET_NULL)
    pharmaceutical_care = models.CharField(max_length=225)
    pharmaceutical_details = models.CharField(max_length=225)
    medication = models.CharField(max_length=225)
    proposed_intervention = models.CharField(max_length=225)
    details = models.TextField(max_length=1000, blank=True, null=True)


class InterventionResponses(models.Model):
    pharmaceutical_care = models.CharField(max_length=225)
    pharmaceutical_details = models.CharField(max_length=225)
    proposed_intervention = models.CharField(max_length=225)


class Medications(models.Model):
    product_name = models.CharField(max_length=225)
