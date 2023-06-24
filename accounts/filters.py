import django_filters
from .models import Account


class AccountFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name="email", lookup_expr="iexact")
    
    class Meta:
        model = Account
        fields = ["email"]
