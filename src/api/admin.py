from django.contrib import admin
from .models import ClientActivity, ClientProduct

admin.site.register(ClientProduct)
admin.site.register(ClientActivity)
