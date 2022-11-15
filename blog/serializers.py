from dataclasses import fields
from rest_framework import serializers
from .models import *

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class AboutHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHeader
        fields = '__all__'


class AboutHeader_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHeader_2
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):

    image_1 = serializers.ImageField(required=False)
    image_2 = serializers.ImageField(required=False)
    image_3 = serializers.ImageField(required=False)
    image_4 = serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields = ('image_1','image_2','image_3','image_4','description')

    def create(self, validated_data):
        instance = Product.objects.create(
            **validated_data
        )
        return instance

class CreateSolutionSerializer(serializers.ModelSerializer):

    image_1 = serializers.ImageField(required=False)
    image_2 = serializers.ImageField(required=False)
    image_3 = serializers.ImageField(required=False)
    image_4 = serializers.ImageField(required=False)
    class Meta:
        model = Solution
        fields = ('image_1','image_2','image_3','product','image_4','description')

    def create(self, validated_data):
        instance = Solution.objects.create(
            **validated_data
        )
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class GeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettings
        fields = '__all__'


class CreateInstructorSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)
    class Meta:
        model = Instructor
        fields = '__all__'

    def create(self, validated_data):
        instance = Product.objects.create(
            **validated_data
        )
        return instance


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
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