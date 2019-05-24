from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def user_login(request):
	
	return render(request, "login.html", )


def user_singup(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('exchange')
	else:
		form = UserCreationForm()

	context = {
		'form':form
	}
	
	return render(request, "singup.html",context )


def user_forgot(request):

	return render(request, "forgot.html")		