from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from core.a1.x9f import X9F
from django.conf import settings
import stripe
import random

stripe.api_key = settings.STRIPE_SECRET_KEY

# API Health Check
def model_list(request):
    return JsonResponse({
        "status": "API is live!",
        "endpoints": {
            "/predict": "POST - Get a prediction (costs 1 credit)",
            "/credits": "GET - Check your credits",
            "/stripe/checkout": "POST - Buy more credits"
        }
    })

# ML Prediction Endpoint
@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            user = request.user  # Requires authentication
            credits, _ = UserCredits.objects.get_or_create(user=user)
            
            if credits.credits < 1:
                return JsonResponse({"error": "Insufficient credits"}, status=402)
                
            credits.credits -= 1
            credits.save()
            
            return JsonResponse(X9F.predict(request.body.decode()))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# Stripe Checkout
@csrf_exempt
def stripe_checkout(request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': settings.STRIPE_PRICE_ID,
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/payment/success/'),
            cancel_url=request.build_absolute_uri('/payment/cancel/'),
            metadata={
                "user_id": request.user.id if request.user.is_authenticated else "anon"
            }
        )
        return JsonResponse({
            "status": "success",
            "mock_payment": {
                "id": session.id,
                "credits_added": 100,
                "receipt_url": session.url
            }
        })
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "error": str(e)
        }, status=400)

# Stripe Webhook
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get('Stripe-Signature')
    try:
        event = stripe.Webhook.construct_event(
            payload, 
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            user = User.objects.get(id=session.metadata.user_id)
            credits, _ = UserCredits.objects.get_or_create(user=user)
            credits.credits += 100
            credits.save()
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=400)

# Credit Balance
def credit_balance(request):
    user = request.user  # Requires auth 
    credits = UserCredits.objects.get_or_create(user=user)[0]
    return JsonResponse({"credits": credits.credits})