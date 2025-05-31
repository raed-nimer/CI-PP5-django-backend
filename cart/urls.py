from django.urls import path
from .views import (
    CartItemsView,
    AddToCartView,
    UpdateCartItemView,
    DeleteCartItemView
)

urlpatterns = [
    path(
        '',
        CartItemsView.as_view(),
        name='get_cart_items'
    ),
    path(
        'add/',
        AddToCartView.as_view(),
        name='add_to_cart'
    ),
    path(
        'update/<int:pk>/',
        UpdateCartItemView.as_view(),
        name='update_cart_item'
    ),
    path(
        'delete/<int:pk>/',
        DeleteCartItemView.as_view(),
        name='delete_cart_item'
    ),
]
