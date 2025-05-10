from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductListView.as_view(), name="products"), # /products
]

# urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)