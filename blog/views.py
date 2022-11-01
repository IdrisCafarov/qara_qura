from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(['GET'])
def about_view(request):
    if request.method == 'GET':
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def about_header_view(request):
    if request.method == 'GET':
        about = AboutHeader.objects.all()
        serializer = AboutHeaderSerializer(about, many=True)
        return Response(serializer.data)

class ProductCreateView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        return serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.filter(draft=True)
    parser_classes = (MultiPartParser, FormParser)
    
    # pagination_class = CustomPagination

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     queryset = Product.objects.all()
    #     # category = request.GET.get("category", None)
    #     # search = request.GET.get("search", None)
    #     # if category:
    #     #     queryset = queryset.filter(subcategory__category__id=int(category))
    #     return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializer
        return CreateProductSerializer

    def perform_create(self, serializer):
        return serializer.save()

# class product_detail(viewsets.ModelViewSet):
#     # queryset = Product.objects.filter(draft=True)
    
#     parser_classes = (MultiPartParser, FormParser)
#     lookup_field = "id"
    
    
#     def get_queryset(self, *args, **kwargs):
#         id = self.kwargs["id"]
        
#         queryset = get_object_or_404(Product,id=id,draft=True)

#         return queryset

#     def get_serializer_class(self):
#         if self.request.method == "GET":
#             return ProductSerializer
#         return CreateProductSerializer

#     def perform_create(self, serializer):
#         return serializer.save()



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