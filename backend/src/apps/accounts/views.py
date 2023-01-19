from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate,login
# from .forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages

class IndexView(TemplateView):
    template_name = "index.html"
index_page = IndexView.as_view()

# Login started
def user_login(request):
    if request.method == 'POST':
        user = authenticate(request,
                            email = request.POST['email'],
                            password = request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse('Authenticated succesfully')
            else:
                return HttpResponse("O'chirilgan hisob")
        else:
            return HttpResponse("Noto'g'ri Login")   
    else:
        
        form = login
    return render(request,'account/signin.html',{'form':form})                                             
# Login ended


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="account/register.html", context={"register_form":form})
	
