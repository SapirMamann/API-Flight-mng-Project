from rest_framework import serializers

from ..models import AirlineCompany


class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineCompany
        fields = ('name','id',)     #delete id 
        

    def validate_name(self, value):
        if len(value) < 3 or len(value) > 100:
            raise serializers.ValidationError('Name has to be between 2 and 100.')
        return value
