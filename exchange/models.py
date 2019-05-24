from django.db import models

# Create your models here.

class PaymentMethod(models.Model):
	WEIGHT_LIST = (
        ('Gram', 'Gram'),
    )
	name = models.CharField(max_length=150)
	image = models.ImageField(upload_to = 'uploaded_images/', default='SOME STRING')
	available_amount = models.IntegerField()
	weight = models.CharField(max_length=10, choices=WEIGHT_LIST,blank=True,null=True)
	price = models.FloatField(blank=True,null=True)

	#string method
	def __str__(self):
		return self.name
	


class ExchangeRate(models.Model):
	from_PM = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, blank=True, null=True, related_name='exchange_rate_from_PM') # PM = payment method
	to_PM = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, blank=True, null=True, related_name='exchange_rate_to_PM') # PM = payment method
	rate = models.FloatField(blank=True,null=True)
	is_available = models.BooleanField(default=True, blank=True, null=True)



class TransactionForm(models.Model):

	STATUS_LIST = (
        ('Processing', 'Processing'),
        ('Done', 'Done'),
        ('Failed', 'Failed'),
    )

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	sendAmount = models.CharField(max_length=100)
	sendFrom = models.CharField(max_length=100)
	receiveAmount = models.CharField(max_length=100)
	receiveFrom = models.CharField(max_length=100)
	transaction_at = models.DateTimeField(auto_now=True, blank=True, null=True,)
	status = models.CharField(max_length=10, default='Processing', choices=STATUS_LIST,blank=True,null=True) 	