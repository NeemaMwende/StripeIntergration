from django.conf import settings
from django.shortcuts import render, redirect
import stripe

# Stripe configuration
stripe.api_key = settings.STRIPE_SECRET_KEY

# Checkout session creation view
def create_checkout_session(request):
    YOUR_DOMAIN = 'http://localhost:8000'  # Replace with your domain

    try:
        # Create a new Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Cool Product',
                        },
                        'unit_amount': 2000,  # 2000 cents = $20
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

# Success page view
def success(request):
    return render(request, 'success.html')

# Cancel page view
def cancel(request):
    return render(request, 'cancel.html')
