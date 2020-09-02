from django.contrib import admin
from .models import Send_email
# Register your models here.

class SendEmailAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'for_send_email']


admin.site.register(Send_email, SendEmailAdmin)