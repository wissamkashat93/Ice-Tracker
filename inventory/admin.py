from django.contrib import admin

from .models import sizes, flavor, shipping

admin.site.register(flavor)
admin.site.register(sizes)
admin.site.register(shipping)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','flavor','size')

# Register your models here.
