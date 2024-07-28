from django.apps import AppConfig
from config import settings
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class BookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "book"
    verbose_name = "Book"

    def ready(self):
        """
        Configure periodic tasks when the application is ready.
        This method sets up an interval schedule and a periodic task to send an email periodically
        """
        interval, created = IntervalSchedule.objects.get_or_create(
            every=settings.TASK_SCHEDULE_MINUTES,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.update_or_create(
            name="Send periodic email",
            defaults={
                "interval": interval,
                "task": "book.tasks.send_message_for_user",
            },
        )
