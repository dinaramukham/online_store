from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from pytils.translit import slugify
from . import models
from .models import Blog


# Create your views here.
# BlogListView
class BlogListView(ListView):
    model = models.Blog
    template_name = 'blog/index.html'
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True )
        return queryset

class BlogDetailView(DetailView):
    model = models.Blog
    template_name = 'blog/detail.html'
    def get_object(self, queryset=None ):
        self.object = super().get_object(queryset )
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView):
    models = models.Blog

    fields = ['title']
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:blog_list')
    def form_valid(self, form):
        if form.is_valid():
            new_mat=form.save()
            new_mat.slug=slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form )
class BlogDeleteView(DeleteView):
    models = models.Blog
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    models = models.Blog
    fields = ['title']
    template_name = 'blog/update.html'
    #success_url = reverse_lazy('blog:blog_list')
    def form_valid(self, form):
        if form.is_valid():
            new_mat=form.save()
            new_mat.slug=slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form )
    def get_success_url(self):
        return reverse('blog:blog_update', args= [self.kwargs.get('pk')] )