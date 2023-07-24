from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from .forms import ProductForm
from .models import Product
import os


def create(request):
    context = {}

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            element = form.save()
            context['element'] = element
    else:
        form = ProductForm()

    context['form'] = form
    return render(request, 'products/create.html', context)


class ProductListView(ListView):
    model = Product
    fields = ['name', 'country_id', 'manufacturer_id', 'number_id']
    template_name = 'products/list.html'
    context_object_name = 'produits'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'country_id', 'manufacturer_id', 'number_id']
    template_name = 'products/create.html'
    success_url = reverse_lazy("list")
    context_object_name = 'produits'


class ProductDetailView(DetailView):
    model = Product
    fields = ['pk', 'name', 'country_id', 'manufacturer_id', 'number_id', 'barcode']
    template_name = 'products/detail.html'
    success_url = reverse_lazy('list')
    context_object_name = 'produits'


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'produits'
    template_name = 'products/delete.html'
    success_url = reverse_lazy("list")



class ProductUpdateView(UpdateView):
    model = Product
    context_object_name = 'produits'
    template_name = 'products/update.html'
    form_class = ProductForm
    success_url = reverse_lazy("list")

