from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import contact

# Create your views here. 

@login_required
def contact_main(request):

	if request.method == 'POST':
		form = contact(request.POST, request.FILES)

		if form.is_valid():
			form.save()

	else:
		form = contact()

	context = {
		'form': form
	}
	
	return render(request, "contact.html", context)


def terms_main(request):
	
	return render(request, "terms.html", )	
