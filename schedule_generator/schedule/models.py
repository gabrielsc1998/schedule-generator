from django.db import models

from ministry.models import Ministry, MinistryActivity, Member


class Schedule(models.Model):
    initial_date = models.DateField(
        verbose_name='Data inicial'
    )
    final_date = models.DateField(
        verbose_name='Data final'
    )
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.CASCADE,
        verbose_name='Ministério'
    )
    activities = models.ManyToManyField(
        MinistryActivity,
        verbose_name='Atividades',
        blank=True
    )
    # schedule = models.JSONField(
    #     verbose_name='Escala',
    #     blank=True
    # )

    class Meta:
        verbose_name = 'Escala'
        verbose_name_plural = 'Escalas'

    def __str__(self):
        return f'Escala do ministério de: {self.ministry}'


class ScheduleRestrictionDate(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='Escala'
    )
    date = models.DateField(
        verbose_name='Data'
    )

    class Meta:
        verbose_name = 'Data de restrição'
        verbose_name_plural = 'Datas de restrição'

    def __str__(self):
        return f'{self.date}'


class ScheduleRestrictions(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='Escala'
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        verbose_name='Membro'
    )
    dates = models.ManyToManyField(
        ScheduleRestrictionDate,
        verbose_name='Datas de restrição',
        blank=True
    )

    class Meta:
        verbose_name = 'Restrições de escala'
        verbose_name_plural = 'Restrições de escala'

    def __str__(self):
        return f'Restrição da escala {self.schedule}'
    