from django.contrib import admin
from .models import PaymentMethod, ExchangeRate,TransactionForm

class PaymentMethodAdmin(admin.ModelAdmin):
	fieldsets = [
		("Payment Method", {"fields": ["name", "available_amount","weight","image","price"]}),
	]

	list_display = ("name", "price", "available_amount", "weight",)
	list_editable = ("available_amount",)



class ExchangeRateAdmin(admin.ModelAdmin):
	fieldsets = [
		("Exchange Rate", {"fields": ["from_PM", "to_PM","rate","is_available"]}),
	]
	list_display = ("from_PM", "to_PM","rate","is_available")
	list_editable = ("rate",)


class TransactionFormAdmin(admin.ModelAdmin):
	fieldsets = [
		("Transaction Rate", {"fields": ["name", "email","phone","sendAmount","sendFrom","receiveAmount","receiveFrom","transaction_at","status"]}),
	]
	list_display = ("name", "email","phone","sendAmount","sendFrom","receiveAmount","receiveFrom","transaction_at","status")	
	list_editable = ("status",)
	

# Register your models here.
admin.site.register(PaymentMethod,PaymentMethodAdmin)
admin.site.register(ExchangeRate,ExchangeRateAdmin)
admin.site.register(TransactionForm,TransactionFormAdmin)
