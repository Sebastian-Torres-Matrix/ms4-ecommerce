from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Shopping bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HSoj8LIeQNknq95rMwforiJLdWhimgHV6UyGw0zYWvKEKdFN4QUdIh1C6RrkXaMvv6divDlNkWnqCWhOBH1FnPR00XKSHxbdD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
