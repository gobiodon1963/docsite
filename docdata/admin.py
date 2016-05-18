from django.contrib import admin
from docdata.models import DocHeader, DocTable, Product, Contractor

class DocHeaderAdmin(admin.ModelAdmin):
    list_display = ('doc_number', 'doc_type', 'doc_date', 'apl_name', 'account', 'total_sum', 'currency')

class DocTableAdmin(admin.ModelAdmin):
    list_display = ('header', 'art', 'name', 'qty', 'unit_id', 'item_sum', 'gtd', 'country_code')
    raw_id_fields = ('header',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('art', 'name', 'unit_id', 'unit_code', 'need_to_import')
    
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('apl_id', 'name', 'inn', 'kpp', 'need_to_import', 'hld')
    
# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(DocHeader, DocHeaderAdmin)
admin.site.register(DocTable, DocTableAdmin)
