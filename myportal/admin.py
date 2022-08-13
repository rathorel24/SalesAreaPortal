from django.contrib import admin
from .models import RetailOutlets, DivOffice

@admin.register(RetailOutlets)
class AdminRetailOutlets(admin.ModelAdmin):
      list_display = [f.name for f in RetailOutlets._meta.fields]
      search_fields = ('code','name',)
      list_filter = ('type','area')

# __all__ can not be used in admin as it is not defined fucntion here -- 'FO_name'


@admin.register(DivOffice)
class AdminDivOffice(admin.ModelAdmin):
        list_display = [f.name for f in DivOffice._meta.fields]
        search_fields = ('id', 'fieldofficer_name',)



#
# list_display = ['code','name','area','sales','FO_name','type']
#
#


