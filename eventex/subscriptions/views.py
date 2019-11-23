from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            body = render_to_string('subscriptions/subscription_email.txt',
                                    context)
            recipient_list = [
                'contato@eventex.com.br',
                form.cleaned_data['email']
            ]
            mail.send_mail(
                subject='Confirmação de inscrição',
                message=body,
                from_email='contato@eventex.com.br',
                recipient_list=recipient_list
            )
            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
        context = {
            'form': form
        }
        return render(
            request,
            'subscriptions/subscription_form.html',
            context
        )

    context = {
        'form': SubscriptionForm()
    }
    return render(
        request,
        'subscriptions/subscription_form.html',
        context
    )
