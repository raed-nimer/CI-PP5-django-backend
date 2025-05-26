from . import views
from django.urls import path


urlpatterns = [
    path('place/', views.PlaceOrderView.as_view(), name='place_order'),
    path('list/', views.ListOrdersView.as_view(), name='list_orders')
]
