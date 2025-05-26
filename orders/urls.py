from .views import place_order
from django.urls import path

urlpatterns = [
    path('place/', place_order, name='place_order'),
    path('list/', ListOrdersView.as_view(), name='list_orders')
]
