from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
# Create your views here.

def data_atual(request):
    agora = datetime.datetime.now()
    html ='<html lang="pt-br"><body><h1>Agora é %s.</h1></body></html>' %agora
    return HttpResponse(html)

class ProductListView (ListView):
    model = Product
    template_name = 'produtos_list.html'
    context_object_name = 'products'
    paginate_by = 10


# CREATE
class ProductCreateView (CreateView):
    model = Product
    fields = ['name', 'image', 'brand', 'category' , 'description', 'rating', 'price', 'countInStock' , 'user']
    template_name = 'product_create_update.html'
    context_object_name = 'product' 
    success_url = reverse_lazy('product-list') 

# READ
class ProductDetailView (DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

# UPDATE

class ProductUpdateView (UpdateView):
    model = Product
    fields = ['name', 'image', 'brand', 'category' , 'description', 'rating', 'price', 'countInStock' , 'user']
    template_name = 'product_create_update.html'
    context_object_name = 'product' 
    success_url = reverse_lazy('product-list') 

# DELETE
class ProductDelete (DeleteView):
    model = Product
    template_name = 'product_confirme_delete.html'
    success_url = reverse_lazy('product-list')