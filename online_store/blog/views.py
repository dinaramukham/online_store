from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from . import models


# Create your views here.
# BlogListView
class BlogListView(ListView):
    model = models.Blog
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = models.Blog
    template_name = 'blog/detail.html'


class BlogCreateView(CreateView):
    models = models.Blog

    fields = ['title']
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:blog_list')
class BlogDeleteView(DeleteView):
    models = models.Blog
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:blog_list')
class BlogUpdateView(UpdateView):
    models = models.Blog
    fields = ['title']
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:blog_list')
