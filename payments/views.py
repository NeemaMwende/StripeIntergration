from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import path
from . import views
from django.conf import settings
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 500,
            currency = 'usd',
            description = 'A django charge',
            source = request.POST['stripeToken']
        )
        return render(request, "charge.html")