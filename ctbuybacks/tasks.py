import logging

from celery import shared_task, chain
import os
import corptools

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from corptools.models import CharacterAudit
from corptools.tasks import update_char_orders

from .models import BuyBackConfig

logger = logging.getLogger(__name__)

@shared_task
def do_market_updates_for_all():
    config = BuyBackConfig.objects.get(pk=1)
    corps = config.corp_filter.all().values_list('corporation_id', flat=True)

    chars = CharacterAudit.objects.filter(character__corporation_id__in=corps).select_related('character')

    for c in chars:
        update_char_orders.apply_async(args=(c.character.character_id,), priority=6)