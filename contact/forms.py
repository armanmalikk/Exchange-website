from django import forms
from .models import contactForm

class contact(forms.ModelForm):



	class Meta:
		model = contactForm
		fields = ('name','email', 'subject','message',)

	def clean(self):

		name =self.cleaned_data.get('name')
		email =self.cleaned_data.get('email')
		subject =self.cleaned_data.get('subject')
		message =self.cleaned_data.get('message')
