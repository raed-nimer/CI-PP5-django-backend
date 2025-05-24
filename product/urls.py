from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductListView.as_view(), name="products"), # /products
    path('categories/', views.CategoryListView.as_view(), name="categories"), # /products/categories
    path('<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"), # /products/1
]

# urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
