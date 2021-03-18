from django_celery_beat.models import PeriodicTask
from datetime import timedelta

PeriodicTask.objects.update(last_run_at=None)