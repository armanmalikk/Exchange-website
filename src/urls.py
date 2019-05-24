"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from exchange.views import exchange_main, get_rate, get_available_exchange
from django.conf import settings
from django.conf.urls.static import static
from user.views import user_login,user_singup,user_forgot
from contact.views import contact_main,terms_main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', exchange_main, name='exchange'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('singup/', user_singup, name='singup'),
    path('forgot/', user_forgot, name='forgot'),
    path('contact/', contact_main, name='contact'),
    path('terms/', terms_main, name='terms'),
    path('get_available_exchange/', get_available_exchange, name='get_available_exchange'),
    path('get_rate/', get_rate, name='get_rate')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)