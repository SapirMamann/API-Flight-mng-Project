from rest_framework import serializers
import re

from ..models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        

    def validate_first_name(self, first_name):
        if len(first_name) < 2 or len(first_name) > 100:
            raise serializers.ValidationError("name length must be between 3 to 99.")     
        if not re.match(r'^[a-zA-Z \-]+$', first_name):
            raise serializers.ValidationError("Name must only contain alphabetic characters.")

        # First name cant contain bad words or spaces
        return first_name
    

    def validate_last_name(self, last_name):
        if len(last_name) < 2 or len(last_name) > 100:
            raise serializers.ValidationError("name length must be between 3 to 99.")     
        if not re.match(r'^[a-zA-Z \-]+$', last_name):
            raise serializers.ValidationError("Last name must only contain alphabetic characters.")
        # First name cant contain bad words or spaces
        return last_name
    

    def validate_address(self, address):
        if len(address) < 2 or len(address) > 100:
            raise serializers.ValidationError("address length must be between 3 to 99.")     
        if not re.match(r'^[a-zA-Z \-]+$', address):
            raise serializers.ValidationError("Address must only contain alphabetic characters.")
        # validate its not all numbers
        return address


    def validate_phone(self, phone):
        if len(phone) != 10:
            raise serializers.ValidationError("Phone length must be exactly 10 numbers.")     
        elif not phone.isnumeric():
            raise serializers.ValidationError("Phone must contain only numbers.")
        return phone
    

    def validate_credit_card(self, credit_card):
        if len(credit_card) != 16:
            raise serializers.ValidationError("credit card length must be exactly 16 numbers.")     
        elif not credit_card.isnumeric():
            raise serializers.ValidationError("credit card must contain only numbers.")
        return credit_card
    

    