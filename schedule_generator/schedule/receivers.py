import datetime

from django.dispatch import receiver
from django.db.models.signals import post_save

from ministry.models import Member, Ministry

from .helpers import ScheduleHelpers
from .models import Schedule, ScheduleRestrictions, ScheduleRestrictionDate


@receiver(post_save, sender=Schedule)
def crete_restritions_for_new_schedule(sender, instance: Schedule, created: bool, **kwargs):
    if created:
        for member in Ministry.objects.get(pk=instance.ministry.pk).members.all():
            ScheduleRestrictions.objects.create(
                schedule=instance,
                member=member
            )
        all_schedule_sundays = ScheduleHelpers.get_all_sundays_between_dates(
            instance.initial_date,
            instance.final_date
        )
        for sunday in all_schedule_sundays:
            ScheduleRestrictionDate.objects.create(
                schedule=instance,
                date=sunday
            )
