from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.


@api_view(['GET'])
def about_view(request):
    if request.method == 'GET':
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_product = serializer.save()
        return Response(serializer.data, status=201)


@api_view(['GET'])
def product_view(request):
    if request.method == 'GET':
        product = Product.objects.filter(draft=True)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_detail(request,id):
    if request.method == 'GET':
        product = Product.objects.filter(draft=True,id=id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = CreateContactSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_product = serializer.save()
        return Response(serializer.data, status=201)