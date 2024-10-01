from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe

# Stripe configuration
stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passing Stripe's publishable key to the template
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

# Handling the charge
def charge(request):
    if request.method == 'POST':
        try:
            # Create the charge using the Stripe API
            charge = stripe.Charge.create(
                amount=500,  # This is in cents, so it represents $5.00
                currency='usd',
                description='Payment Gateway',
                source=request.POST['stripeToken']  # Stripe token from form
            )
        except stripe.error.StripeError as e:
            # Handle error here if payment fails
            return render(request, "error.html", {'error': str(e)})

        return render(request, "charge.html")  # Success page
