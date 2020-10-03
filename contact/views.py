from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_form(request):
    template = 'contact/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Thank you for your message! We will reply as soon as possible. Have a great day!')
            return redirect('products')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, template, context)
