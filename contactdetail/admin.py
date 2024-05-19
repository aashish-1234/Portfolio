from django.contrib import admin
from django.contrib.admin.sites import site
from contactdetail.models import contactDetail
# Register your models here.
class contactdetailAdmin(admin.ModelAdmin):
    list_display=('name','email','message','subject')
admin.site.register(contactDetail,contactdetailAdmin)
