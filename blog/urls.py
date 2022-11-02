from django.urls import path
from .views import *

urlpatterns = [
    # path('',index_view,name="index"),
    path("about_main/", about_view, name="about"),
    path("about_header/", about_header_view, name="about_header"),
    path("about_header_2/", about_header_2_view, name="about_header"),
    path("create_post/", ProductCreateView.as_view({
    'post': 'create'
    }), name="create_post"),
    path("post_list/", ProductListView.as_view({
    'get': 'list',
    }), name="post_list"),
    path("instructor_list/", InstructorListView.as_view({
    'get': 'list',
    }), name="instructor_list"),
    # path("post_detail/<id>/", product_detail.as_view({
    # 'get': 'list'
    # }), name="post_detail"),
    path("create_contact/", ContactCreateView.as_view(), name="create_contact"),
]



