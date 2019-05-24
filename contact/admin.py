from django.contrib import admin
from .models import contactForm

# Register your models here.

class contactAdmin(admin.ModelAdmin):
	fieldsets = [
		("Contact Message", {"fields": ["name", "email","subject","message"]}),
	]

	list_display = ("name", "message", "email", "subject",)


admin.site.register(contactForm,contactAdmin)	
