# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from ..forms.register_form import VerifyForm

# from ...common.sms_sender import SendSMS

# # ... no changes to index() and register() view functions



# @login_required
# def verify_code(request):
#     if request.method == 'POST':
#         form = VerifyForm(request.POST)
#         if form.is_valid():
#             code = form.cleaned_data.get('code')
#             if SendSMS.set_token(request.user.phone, code):
#                 request.user.is_verified = True
#                 request.user.save()
#                 return redirect('index')
#     else:
#         form = VerifyForm()
#     return render(request, 'verify.html', {'form': form})