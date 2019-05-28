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

	has_form_error = False
	form_save_now = False
	form_value = {}

	if request.method == 'POST':
		form = Transaction(request.POST, request.FILES)

		if form.is_valid():

			this_obj = form.save()

			form_save_now =  True
			
			this_obj.sendFrom.available_amount = this_obj.sendFrom.available_amount + this_obj.sendAmount
			this_obj.sendFrom.save()
			this_obj.receiveFrom.available_amount = this_obj.receiveFrom.available_amount - this_obj.receiveAmount
			this_obj.receiveFrom.save()
			# this_obj.save()
		else:
			has_form_error = True
			form_value['sendFrom'] = form.cleaned_data.get('sendFrom')
			form_value['sendAmount'] = form.cleaned_data.get('sendAmount')
			form_value['receiveFrom'] = form.cleaned_data.get('receiveFrom')
			form_value['receiveAmount'] = form.cleaned_data.get('receiveAmount')
			

	else:
		form = Transaction()

	context = {
		'allItems':allItems,
		'form': form,
		'TransactionRequest':TransactionRequest,
		'has_form_error': has_form_error,
		'count':count,
		'form_value':form_value,
		'form_save_now':form_save_now
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
	

	