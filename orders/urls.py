from django.urls import path
from .views import (
    PaymentListCreateView,
    PaymentDetailView,
    OrderListCreateView,
    OrderDetailView,
    OrderProductListCreateView,
    OrderProductDetailView,
)

urlpatterns = [
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    
    path('order-products/', OrderProductListCreateView.as_view(), name='orderproduct-list-create'),
    path('order-products/<int:pk>/', OrderProductDetailView.as_view(), name='orderproduct-detail'),
]

