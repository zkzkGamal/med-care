import django_filters 
from django_filters import CharFilter
from.models import doctor

class DoctorFilter(django_filters.FilterSet):
    name = CharFilter(field_name = 'name' , lookup_expr = 'icontains')
    class Meta:
        model = doctor
        # fields = ['name','specialist','price', 'years_of_experience']
        fields = ['name', 'gender','specialist' , 'years_of_experience' , 'price']
        