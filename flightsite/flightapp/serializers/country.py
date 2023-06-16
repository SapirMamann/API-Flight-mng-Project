from rest_framework import serializers
import re

from ..models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    
    def validate_name(self, name):
        if len(name) < 2 or len(name) > 50:
            raise serializers.ValidationError("Name length must be between 3 to 49.")
        elif not re.match(r'^[a-zA-Z \-]+$', name):
            raise serializers.ValidationError("Name must only contain alphabetic characters.")
        return name
    