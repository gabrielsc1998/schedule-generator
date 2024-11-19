from collections.abc import Callable, Sequence
from typing import Any
from django.contrib import admin
from django.db.models.fields.related import RelatedField
from django.utils.html import format_html
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

import schedule.models as models


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'ministry', 'initial_date', 'final_date', 'generate')
    list_filter = ('ministry',)
    search_fields = ('ministry__name',)
    date_hierarchy = 'initial_date'
    filter_horizontal = ('activities',)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        generate = request.GET.get('e')
        if generate:
            print('Generate to:', generate)
        return super().get_queryset(request)

    def name(self, obj: models.Schedule):
        return f'Escala {obj.pk} do ministério de: {obj.ministry}'
    name.short_description = 'Nome'

    def generate(self, obj: models.Schedule):
        return format_html(
            '<a href="/admin/schedule/schedule/?e={id}">{label}</a>',
            id=obj.pk,
            label='Gerar'
        )
    generate.short_description = 'Gerar'
    

class ScheduleRestrictionsAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'member', 'initial_date', 'final_date', 'restriction_dates')
    list_filter = ('schedule',)
    search_fields = ('schedule__ministry__name',)
    filter_horizontal = ('dates',)

    def schedule(self, obj: models.ScheduleRestrictions):
        return f'Restrição da escala {obj.schedule}'
    schedule.short_description = 'Escala'

    def initial_date(self, obj: models.ScheduleRestrictions):
        return obj.schedule.initial_date
    initial_date.short_description = 'Data inicial'

    def final_date(self, obj: models.ScheduleRestrictions):
        return obj.schedule.final_date
    final_date.short_description = 'Data final'

    def restriction_dates(self, obj: models.ScheduleRestrictions):
        return ', '.join([d.__str__() for d in obj.dates.all()])
    restriction_dates.short_description = 'Datas de restrição'

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)
        user = request.user
        if not user.is_superuser:
            qs = qs.filter(member__user=user)
        return qs

    def get_form(self, request: HttpRequest, obj, **kwargs):
        user = request.user
        if not user.is_superuser:
            kwargs['exclude'] = ('schedule', 'member',)
        return super().get_form(request, obj, **kwargs)

    # def get_field_queryset(self, db, db_field, request):
    #     field_qs = super().get_field_queryset(db, db_field, request)
    #     if db_field.name == 'date':
    #         field_qs = field_qs.filter(schedule=request.user)
    #     return 

admin.site.register(models.Schedule, ScheduleAdmin)
admin.site.register(models.ScheduleRestrictions, ScheduleRestrictionsAdmin)
# admin.site.register(models.ScheduleRestrictionDate)