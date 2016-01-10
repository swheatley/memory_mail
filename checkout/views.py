from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import StripeForm
import stripe 


stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_PUBLIC_KEY
        return context 


class SuccessView(TemplateView):
    template_name = 'checkout/thank_you.html' 


class SubscribeView(StripeMixin, FormView):
    template_name = 'subscribe.html'
    form_class = StripeForm
    sucess_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        customer_data = {
            'description': 'Some Customer Data',
            'card': form.cleaned_data['stripe_token']
        }
        customer = stripe.Customer.create(**customer_data)

        customer.subscriptions.create(plan="basic_plan")

        return super(SubscribeView, self).form_valid(form)


@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            stripe.Customer.retrieve(customer_id)
            customer.sources.create(card=token)
            charge = stripe.Charge.create(
                amount=1000,  # amount in cents, again
                currency="usd",
                customer=customer,
                description="payinguser@example.com"
            )
        except stripe.error.CardError, e:
            #  The card has been declined
            pass
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request, template, context)


