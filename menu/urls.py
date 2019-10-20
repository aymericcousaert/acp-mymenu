from django.urls import path

from menu import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('payment/', views.PaymentMethodView.as_view(), name='payment'),
    path('payments/', views.PaymentMethodListView.as_view(), name='payment_list')
]
