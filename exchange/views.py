from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import PaymentMethod, ExchangeRate, TransactionForm
from .forms import Transaction

# Create your views here.
def exchange_main(request):

	allItems = PaymentMethod.objects.all()
	TransactionRequest = TransactionForm.objects.all()
	count = User.objects.count()

	if request.method == 'POST':
		form = Transaction(request.POST, request.FILES)

		if form.is_valid():
			form.save()

	else:
		form = Transaction()

	context = {
		'allItems':allItems,
		'form': form,
		'TransactionRequest':TransactionRequest,
		'count':count
	}
	
	return render(request, "index.html", context)
	

def get_available_exchange(request):
	request.GET['from'] = 'gold'

	gold = ExchangeRate.objects.all()

	print(gold)	

	return JsonResponse('ja icca', safe=False)



def get_rate(request):

	this_obj_id = request.GET['exchange_obj_id']
	this_payment_method = get_object_or_404(PaymentMethod, id=this_obj_id)
	print(this_payment_method)

	payment = ExchangeRate.objects.filter(from_PM = this_payment_method).values('to_PM', 'to_PM__id', 'rate', 'is_available','to_PM__name','to_PM__image','to_PM__available_amount')
	payment_method = list(payment)

	return JsonResponse(payment_method, safe=False)
	

	