from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import viewsets
from django.shortcuts import get_list_or_404, render
from rest_framework import status


# Create your views here.



# def index_view(request):
#     return render(request,"index.html")

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

@api_view(['GET'])
def about_header_2_view(request):
    if request.method == 'GET':
        about = AboutHeader_2.objects.all()
        serializer = AboutHeader_2Serializer(about, many=True)
        return Response(serializer.data)

class ProductCreateView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['post', ]

    def perform_create(self, serializer):
        return serializer.save()

    def post(self, request, *args, **kwargs):
        documents = request.FILES.getlist('document', None)
        data = {
            "title": request.POST.get('title', None),
            }
        _serializer = self.serializer_class(data=data, context={'documents': documents})
        if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # NOQA


class SolutionCreateView(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = CreateSolutionSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        return serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,many=True)
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



class SolutionListView(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
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
            return SolutionSerializer
        return CreateSolutionSerializer

    def perform_create(self, serializer):
        return serializer.save()



class GeneralSettingsListView(viewsets.ModelViewSet):
    queryset = GeneralSettings.objects.all()
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
            return GeneralSettingsSerializer

    def perform_create(self, serializer):
        return serializer.save()


class InstructorListView(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
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
            return InstructorSerializer
        return CreateInstructorSerializer

    def perform_create(self, serializer):
        return serializer.save()

class product_detail(viewsets.ModelViewSet):
    # queryset = Product.objects.filter(draft=True)
    
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "id"
    
    
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs["id"]
        
        queryset = get_list_or_404(Product,id=id,draft=True)

        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializer
        return CreateProductSerializer

    def perform_create(self, serializer):
        return serializer.save()

class solution_detail(viewsets.ModelViewSet):
    # queryset = Product.objects.filter(draft=True)
    
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "id"
    
    
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs["id"]
        
        queryset = get_list_or_404(Solution,id=id)

        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SolutionSerializer
        return CreateSolutionSerializer

    def perform_create(self, serializer):
        return serializer.save()


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