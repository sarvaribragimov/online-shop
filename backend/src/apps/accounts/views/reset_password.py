from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from ..models import Account
from ...common.timer import timer  # noqa
from ...common.send_email import send_email_async
import asyncio

# @timer
def forgot_password(request):
    if request.method != "POST":  # if not post request, Guard Clause style
        return render(request, "accounts/forgot_password.html")
    email = request.POST.get("email")
    if Account.objects.filter(email=email).exists():
        user_account = Account.objects.get(email=email)
        current_site = get_current_site(request)
        domain = f"http://{current_site.domain}/verify-password/{urlsafe_base64_encode(force_bytes(user_account))}/"
        subject = "Please reset your password"
        message = "Hi. Please reset your password, click on the link below"
        body = render_to_string(
            "accounts/reset_password.html",
            {
                "subject": subject,
                "body": message,
                "domain": domain,
            },
        )
        html_body = strip_tags(body)
        asyncio.run(send_email_async(subject, html_body, [email]))  # async call
        messages.success(request, "Please check your email")
        return redirect("accounts:login")
    messages.error(request, "Email does not exist")
    return redirect("accounts:register")


def validate_password(request, uidb64):
    if request.method != "POST":  # guard clause
        return render(request, "accounts/validate_password.html")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    if password == confirm_password:
        User = get_user_model()
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, email=uid)
        user.set_password(password)
        user.save()
        messages.success(request, "Password reset successfully")
        return redirect("accounts:login")
    messages.error(request, "Passwords do not match")
    return redirect("/")
