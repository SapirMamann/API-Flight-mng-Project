from rest_framework import serializers

from ..models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    
    def validate_name(self, name):
        if len(name) < 2 or len(name) > 100:
            raise serializers.ValidationError("name length must be between 3 to 99.")     
        # elif name contains bad words
        return name
    
    