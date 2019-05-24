from django import forms
from .models import TransactionForm

class Transaction(forms.ModelForm):



	class Meta:
		model = TransactionForm
		fields = ('name','email', 'phone','sendAmount','sendFrom','receiveAmount','receiveFrom')

	def clean(self):

		name =self.cleaned_data.get('name')
		email =self.cleaned_data.get('email')
		phone =self.cleaned_data.get('phone')
		sendAmount =self.cleaned_data.get('sendAmount')
		sendFrom =self.cleaned_data.get('sendFrom')
		receiveAmount =self.cleaned_data.get('receiveAmount')
		receiveFrom =self.cleaned_data.get('receiveFrom')




		super(Transaction, self).clean()	