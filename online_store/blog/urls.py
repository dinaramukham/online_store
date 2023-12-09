from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from online_store.blog import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
