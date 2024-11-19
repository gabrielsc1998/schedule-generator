from django.db import models


class MinistryType():
    MUSIC = 1
    KIDS = 2
    TRANSMISSION = 3
    COMUNICATION = 4

    mapper = {
        MUSIC: 'Música',
        KIDS: 'Crianças',
        TRANSMISSION: 'Transmissão',
        COMUNICATION: 'Comunicação',
    }

    def choices():
        return ((key, value) for key, value in MinistryType.mapper.items())
    
    def get_type_name(type):
        return MinistryType.mapper.get(type)
    

class Ministry(models.Model):
    type = models.IntegerField(
        choices=MinistryType.choices(),
        verbose_name='Tipo'
    )
    members = models.ManyToManyField(
        'Member',
        verbose_name='Membros',
        blank=True,
        related_name='ministry_members'
    )

    class Meta:
        verbose_name = 'Ministério'
        verbose_name_plural = 'Ministérios'

    def __str__(self):
        return MinistryType.get_type_name(self.type)


class MinistryActivity(models.Model):
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.CASCADE,
        verbose_name='Ministério'
    )
    activity = models.CharField(
        max_length=100,
        verbose_name='Atividade'
    )

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return f'{MinistryType.get_type_name(self.ministry.type)} - {self.activity}'


class Member(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )
    activities = models.ManyToManyField(
        MinistryActivity,
        verbose_name='Atividades',
        blank=True
    )

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        return self.user.username
