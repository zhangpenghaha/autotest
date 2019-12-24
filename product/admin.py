from django.contrib import admin
from product.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['productname', 'productdesc', 'producter', 'create_time', 'id']
admin.site.register(Product)


from apitest.models import Apitest,Apis
class ApisAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']
    model = Apis
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','create_time','id']
    inlines = [ApisAdmin]


from webtest.models import Webcase
class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult','create_time','id','product']
    model = Webcase
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','create_time','id']
    inlines = [WebcaseAdmin]