from django.contrib import admin
from receipts.models import Receipt, Item

# Register your models here.
@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass