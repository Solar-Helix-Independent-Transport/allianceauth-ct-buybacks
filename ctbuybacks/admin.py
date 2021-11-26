from django.contrib import admin
from .models import BuyBackConfig
# Register your models here.

@admin.register(BuyBackConfig)
class BuyBackConfigAdmin(admin.ModelAdmin):
    filter_horizontal = ('corp_filter',)

    select_related=True


