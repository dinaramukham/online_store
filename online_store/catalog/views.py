from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import  Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/info_products.html'



def contacts(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
    print(request.method)
    return render(request, 'catalog/contacts.html')


