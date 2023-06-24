from django.db.models.signals import post_save
from .models import Account, Profile, Employer



def create_profile(sender, instance, created, **kwargs):
    if created:
        profile_instance = Profile.objects.create(
            account = instance
        )
        Employer.objects.create(
            profile = profile_instance
        )

post_save.connect(create_profile, Account)