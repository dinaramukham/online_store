from django.shortcuts import render
from django.views.generic import ListView

#from online_store.blog.models import Blog


# Create your views here.
#BlogListView
class BlogListView(ListView):
    model = Blog
    template_name = 'index'
