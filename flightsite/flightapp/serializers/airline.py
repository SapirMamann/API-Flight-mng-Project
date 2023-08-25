from rest_framework import serializers

from ..models import AirlineCompany
from .country import CountrySerializer

class AirlineCompanySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = AirlineCompany
        fields = '__all__'
        

    def validate_name(self, name):
        if len(name) < 2 or len(name) > 100:
            raise serializers.ValidationError('Name length must be between 3 to 99.')
        return name
