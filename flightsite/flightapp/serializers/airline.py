from rest_framework import serializers

from ..models import AirlineCompany


class AirlineCompanySerializer(serializers.ModelSerializer):
    # Used to display the country name instead of the country id
    # country = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = AirlineCompany
        fields = '__all__' #('name','id',)     #delete id 
        

    def validate_name(self, name):
        if len(name) < 2 or len(name) > 100:
            raise serializers.ValidationError('Name length must be between 3 to 99.')
        return name
