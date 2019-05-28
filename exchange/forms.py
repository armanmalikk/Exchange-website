from django import forms
from .models import TransactionForm, PaymentMethod

class Transaction(forms.ModelForm):



	class Meta:
		model = TransactionForm
		fields = ('name','email', 'phone','sendAmount','sendFrom','receiveAmount','receiveFrom')

	def clean(self, *args, **kwargs):
		super().clean(*args, **kwargs)



	def clean(self,*args,**kwargs):

		receiveFrom = self.cleaned_data.get('receiveFrom')
		receiveAmount = self.cleaned_data.get('receiveAmount')

		print('receiveFrom', receiveFrom)
		print('receiveAmount', receiveAmount)
		print('avaiable', receiveFrom.available_amount)

		sendAmount = self.cleaned_data.get('sendAmount')

		if receiveFrom.available_amount < receiveAmount:
			raise forms.ValidationError("amount is not avaiable")

		return super().clean(*args,**kwargs)			




		#super(Transaction, self).clean()	