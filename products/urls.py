from django.contrib import admin
from django.urls import path, include, re_path

from .views import ProductCreateView, ProductListView, ProductDetailView, ProductDeleteView, ProductUpdateView
from . import views

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/edit', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('list/', ProductListView.as_view(), name='list'),
    # path('detail/<str:pk>/', ProductDetailView.as_view(), name='detail'),
    # path('', views.create, name='create'),

]