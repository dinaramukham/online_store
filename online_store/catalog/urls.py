from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('contacts/', views.contacts),
    path('blog/', include('blog.urls')),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product'),

]
