import os

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from corptools.models import CharacterMarketOrder
from .models import BuyBackConfig

@login_required
@permission_required("ctbuybacks.basic_access")
def buyback_list(request, corp_id=None):
    config = BuyBackConfig.objects.get(pk=1)
    orders = []
    corps = config.corp_filter.all().values_list('corporation_id', flat=True)
    orders = CharacterMarketOrder.objects.filter(character__character__corporation_id__in=corps,
                                                 is_buy_order=True,
                                                 state="active"
                                            ).select_related("character",
                                                             "character__character",
                                                             "type_name")

    context = {
        'orders': orders
    }

    return render(request, 'ctbuybacks/list.html', context=context)  # render to template
