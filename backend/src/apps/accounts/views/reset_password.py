from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
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


def forgot_password(request):
    if request.method == "POST":
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
            sendmail = EmailMessage(
                subject=subject,
                body=html_body,
                to=[email],
            )
            messages.success(request, "Please check your email")
            sendmail.send()
            return redirect("accounts:login")
        messages.error(request, "Email does not exist")
        return redirect("accounts:register")
    return render(request, "accounts/forgot_password.html")


def validate_password(request, uidb64):
    if request.method == "POST":
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
    return render(request, "accounts/validate_password.html")
