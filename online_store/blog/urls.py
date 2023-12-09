from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update'),
#    path('published/<int:pk>/', views.published, name='blog_published'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
