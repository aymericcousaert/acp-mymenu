from django.urls import path, include
from django.contrib.auth import views as auth_views
from menu import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>/description', views.ProductDescription.as_view(), name='productDescription'),
    path('payments/', views.PaymentMethodListView.as_view(), name='payment_list'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('form_suggestions/<token_url>', views.FormSuggestionsView.as_view(), name='formSuggestions')
]


