from django.urls import path, include
from django.conf import settings
from contact.views import terms_main,contact_main



urlpatterns = [
    	path('', terms_main, name='terms'),
    	path('contact/', contact_main, name='contact'),
]

