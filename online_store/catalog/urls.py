from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('contacts/', views.contacts),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product')
]