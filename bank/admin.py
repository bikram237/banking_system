from django.contrib import admin

admin.site.site_header="THE INTERN BANK"

class usersadmin(admin.ModelAdmin):
    list_display =['id', 'username', 'email_id', 'contact', 'balance'] 
    search_fields =['username']

class DepositAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'amount']
    search_fields =['username']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'amount', 'action', 'status']
    search_fields =['username']

# Register your models here.
from .models import users
from .models import Deposit
from .models import History

admin.site.register(users,usersadmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(History, HistoryAdmin)