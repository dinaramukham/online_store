from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('contacts/', views.contacts),
    path('blog/', include('blog.urls')),
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('create_product/', views.ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),


]
