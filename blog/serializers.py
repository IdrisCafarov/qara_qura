from dataclasses import fields
from rest_framework import serializers
from .models import *

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields = ('image','description')

    def create(self, validated_data):
        instance = Product.objects.create(
            **validated_data
        )
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        instance = Contact.objects.create(
            **validated_data
        )
        return instance