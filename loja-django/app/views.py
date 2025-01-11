from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import ListView
from .models import Product
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
