from rest_framework import serializers
from .models import Item
from rest_framework.exceptions import ValidationError


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('category', 'subcategory', 'name', 'amount')
        # fields = '__all__'

    @staticmethod
    def validate_amount(data):
        if data <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return data
