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
        name = self.context['name']
        surname = self.context['surname']
        social_link = self.context['social_link']



        # print(documents)
        # post = Product.objects.create(**validated_data)
        post = "smth"
        for document in documents:
            # print(document)
            post = Product.objects.create(image=document, name=name, surname=surname, social_link=social_link)
        return post


    class Meta:
        model = Product
        fields = ('image','name','surname','social_link')

class CreateSolutionSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)



    def create(self, validated_data):
        instance = Solution.objects.create(
            **validated_data
        )
        return instance
    # def create(self, validated_data):
    #     documents = self.context['documents']
    #     # print(documents)
    #     post = Solution.objects.create(**validated_data)
    #     for document in documents:
    #         # print(document)
    #         Solution.objects.create(image=document)
    #     return post

    class Meta:
        model = Solution
        fields = ('image','product','name','surname','social_link')

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



########################################## Portfolio ###################3
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = '__all__'

class ProjectTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImagesSerializer(many=True)
    technology = ProjectTechSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'



class PortfolioSerializer(serializers.ModelSerializer):

    # images = ProductImagesSerializer(many=True)
    experience = ExperienceSerializer(many=True)
    certificate = CertificateSerializer(many=True)



    projects = ProjectSerializer(many=True)
    education = EducationSerializer(many=True)
    specialization = SpecializationSerializer(many=True)
    skills = SkillsSerializer(many=True)
    class Meta:
        model=Portfolio
        fields='__all__'



