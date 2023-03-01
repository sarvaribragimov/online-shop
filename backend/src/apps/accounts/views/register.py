import asyncio

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.db import transaction
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

from ...common.sms_sender import SendSMS
from ...cart.models import Cart
from ...common.get_cart_id import _cart_id
from ...common.send_email import send_email_async
from ..forms.register_form import RegistrationForm


@transaction.atomic
def register(request):
    try:
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                with transaction.atomic():
                    new_form = form.save(commit=False)
                    # data
                    phone_number = form.cleaned_data.get("phone_number")
                    firstname = form.cleaned_data.get("firstname")
                    username = firstname  # get username from email
                    password = form.cleaned_data.get("password")
                    new_form.username = username
                    new_form.phone_number = phone_number
                    new_form.set_password(password)
                    new_form.save()
                    
                    sms = SendSMS()
                    code = sms.generate_one_time_sms()
                    
                    
                    # Email data
                    current_site = get_current_site(request)
                    domain = f"http://{current_site.domain}/activate/{urlsafe_base64_encode(force_bytes(new_form))}/"
                    subject = "Welcome to the site"
                    message = f"Hi {firstname}, welcome to the site"
                    body = render_to_string(
                        "accounts/verification.html",
                        {
                            "subject": subject,
                            "body": message,
                            "domain": domain,
                        },
                    )
                    result = sms.send_sms(
                        phone_number,
                        body,
                    )
                    # html_body = strip_tags(body)
                    # asyncio.run(send_email_async(subject, html_body, [email]))
                    # TODO filter by session key
                    cart, _= Cart.objects.get_or_create(cart_id_pk=_cart_id(request))
                    cart.user = new_form
                    cart.save()

                messages.success(request, f"Account created for {username}!")
                return redirect("accounts:login")
        return render(request, "accounts/register.html", {"form": form})
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect("accounts:register")
