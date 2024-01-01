from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ProductForm, VersionForm
from .models import Product, Version
#from ..users.models import User


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/info_products.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/register/'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user  = self.request.user
        self.object.save()
        return super().form_valid(form )

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/register/'

    model = Product
    form_class = ProductForm

    success_url = reverse_lazy('users_login')
    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        #if self.object.user == User.objects.get(pk=self.kwargs.get('pk')   ) :

        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object   )
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
    print(request.method)
    return render(request, 'catalog/contacts.html')
