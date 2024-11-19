from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    name = 'schedule'
    verbose_name = 'Escalas'

    def ready(self):
        import schedule.receivers
