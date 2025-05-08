from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # Core API Endpoints
    path('', views.model_list, name='api-root'),
    path('models/', views.model_list, name='model-list'),
    
    # Prediction System
    path('predict/', views.predict, name='predict'),
    path('credits/', views.credit_balance, name='credit-balance'),
    
    # Stripe Payment Integration
    path('stripe/checkout/', views.stripe_checkout, name='stripe-checkout'),
    path('stripe/webhook/', views.stripe_webhook, name='stripe-webhook'),
    
    # Admin Interface
    path('admin/', admin.site.urls),
]