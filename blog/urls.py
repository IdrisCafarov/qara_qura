from django.urls import path
from .views import *

urlpatterns = [
    path("about/", about_view, name="about"),
    path("create_post/", ProductCreateView.as_view(), name="create_contact"),
    path("post_list/", product_view, name="post_list"),
    path("post_detail/<id>/", product_detail, name="post_detail"),
    path("create_contact/", ContactCreateView.as_view(), name="create_contact"),
]



