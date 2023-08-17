from rest_framework import serializers
import re

from ..models import Administrator


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'

    def validate_first_name(self, first_name):
        if len(first_name) < 2:
            raise serializers.ValidationError('Must have at least 3 characters')
        if not re.match(r'^[a-zA-Z \-]+$', first_name):
            raise serializers.ValidationError("Name must only contain alphabetic characters.")
        # First name cant contain bad words or spaces
        return first_name
    
    
    def validate_last_name(self, last_name):
        if len(last_name) < 2:
            return serializers.ValidationError('Must have at least 3 characters')
        if not re.match(r'^[a-zA-Z \-]+$', last_name):
            raise serializers.ValidationError("Last name must only contain alphabetic characters.")
        return last_name
    
