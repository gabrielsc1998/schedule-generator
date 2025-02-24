# Generated by Django 5.1 on 2024-09-23 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ministry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateField(verbose_name='Data inicial')),
                ('final_date', models.DateField(verbose_name='Data final')),
                ('activities', models.ManyToManyField(blank=True, to='ministry.ministryactivity', verbose_name='Atividades')),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ministry.ministry', verbose_name='Ministério')),
            ],
            options={
                'verbose_name': 'Escala',
                'verbose_name_plural': 'Escalas',
            },
        ),
        migrations.CreateModel(
            name='ScheduleRestrictionDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule', verbose_name='Escala')),
            ],
            options={
                'verbose_name': 'Data de restrição',
                'verbose_name_plural': 'Datas de restrição',
            },
        ),
        migrations.CreateModel(
            name='ScheduleRestrictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.ManyToManyField(blank=True, to='schedule.schedulerestrictiondate', verbose_name='Datas de restrição')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ministry.member', verbose_name='Membro')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule', verbose_name='Escala')),
            ],
            options={
                'verbose_name': 'Restrições de escala',
                'verbose_name_plural': 'Restrições de escala',
            },
        ),
    ]
