from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate,login
# from .forms import LoginForm
from django.http import HttpResponse
# Create your views here.


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

