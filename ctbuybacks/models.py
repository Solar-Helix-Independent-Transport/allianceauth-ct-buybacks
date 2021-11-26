from allianceauth.eveonline.models import EveCorporationInfo
from django.db import models
from django.core.exceptions import ValidationError

class BuyBackConfig(models.Model):

    corp_filter = models.ManyToManyField(EveCorporationInfo, blank=True,
                                             help_text='Corporations to show in the list')

    time_between_updates = models.IntegerField(default=20,
                                                   help_text='How often should we try to update the orders.')

    def save(self, *args, **kwargs):
        if not self.pk and BuyBackConfig.objects.exists():
            # Force a single object
            raise ValidationError('Only one Settings Model can there be at a time! No Sith Lords there are here!')
        self.pk = self.id = 1 # If this happens to be deleted and recreated, force it to be 1
        return super().save(*args, **kwargs)

    class Meta:
        permissions = (('basic_access', 'Can access buybacks module.'),)
