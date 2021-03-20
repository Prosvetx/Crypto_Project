import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crypto_Project.settings')

app = Celery('Crypto_Project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_data_30s': {
        'task': 'coins.tasks.get_coins_data',
        'schedule': 30.0
        }
    }

app.autodiscover_tasks()
