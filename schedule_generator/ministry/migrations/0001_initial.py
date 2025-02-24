# Generated by Django 5.1 on 2024-09-23 19:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Música'), (2, 'Crianças'), (3, 'Transmissão'), (4, 'Comunicação')], verbose_name='Tipo')),
                ('members', models.ManyToManyField(blank=True, related_name='ministry_members', to='ministry.member', verbose_name='Membros')),
            ],
            options={
                'verbose_name': 'Ministério',
                'verbose_name_plural': 'Ministérios',
            },
        ),
        migrations.CreateModel(
            name='MinistryActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100, verbose_name='Atividade')),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ministry.ministry', verbose_name='Ministério')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='activities',
            field=models.ManyToManyField(blank=True, to='ministry.ministryactivity', verbose_name='Atividades'),
        ),
    ]
