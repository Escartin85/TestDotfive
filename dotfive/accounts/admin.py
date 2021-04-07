from django.contrib import admin

# Register your models here.
from accounts.models import Item

class ItemAdmin(admin.ModelAdmin):
    
	list_display = ["label", "slug", "date_created"]
	list_display_links = ["label"]
	list_filter = ["label"]
	search_fields = ["label"]
	

	class Meta:
		model = Item
  
admin.site.register(Item, ItemAdmin)