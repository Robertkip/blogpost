from django.urls import path
from .views import blog_index, blog_category, blog_detail, search

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("post/<int:pk>/", blog_detail, name="blog_detail"),
    path("category/<category>/", blog_category, name="blog_category"),
    path("search/", search, name="search"),
]