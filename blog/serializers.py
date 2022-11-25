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

    # image = serializers.ImageField(required=False)
    
    # class Meta:
    #     model = Product
    #     fields = ('image','description')

    # def create(self, validated_data):
    #     instance = Product.objects.create(
    #         **validated_data
    #     )
    #     return instance

    def create(self, validated_data):
        documents = self.context['documents']
        # print(documents)
        post = Product.objects.create(**validated_data)
        for document in documents:
            # print(document)
            Product.objects.create(image=document)
        return post
        

    class Meta:
        model = Product
        fields = ('image',)

class CreateSolutionSerializer(serializers.ModelSerializer):

    # image = serializers.ImageField(required=False)
    
    # class Meta:
    #     model = Solution
    #     fields = ('image','product','description')

    # def create(self, validated_data):
    #     instance = Solution.objects.create(
    #         **validated_data
    #     )
    #     return instance
    def create(self, validated_data):
        documents = self.context['documents']
        product_id = self.context['product_id']
        for id in product_id:
            new_id = id
        # print(documents)
        post = Solution.objects.create(**validated_data)
        for document in documents:
            # print(document)
            Solution.objects.create(image=document,product_id=new_id)
        return post

    class Meta:
        model = Solution
        fields = ('image',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        return response


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        return response


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