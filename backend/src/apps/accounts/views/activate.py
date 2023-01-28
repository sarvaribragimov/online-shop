# import force_text
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect

# get_user_model() returns the User model that is active in this project.
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib import messages

# expired link


def activate(request, uidb64):
    try:
        User = get_user_model()
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(email=uid)
        user.is_active = True
        user.save()
        messages.success(request, "Account activated successfully")
        return redirect("accounts:login")
    except Exception:
        return HttpResponse("Invalid activation link")
