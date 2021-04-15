from time import sleep
import datetime

from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

from celery import shared_task
from backend.celery import app
from backend.celery import app

@shared_task
def send_f_gmail(mail_title,mail_description, **kwargs):
    send_mail(
        mail_title,
        mail_description,
        'rishabh.bansal2299123@gmail.com',
        ['rishabh.bansal2299@gmail.com'],
        fail_silently=False,
    )


@shared_task
def duplicate_send_f_gmail(mail_title,mail_description,s_date,**kwargs):
    if cache.get(s_date):
        return
    else:
        cache.set(s_date, 'new')
    sleep(11)
    send_mail(
        mail_title,
        mail_description,
        'rishabh.bansal2299123@gmail.com',
        ['rishabh.bansal2200@gmail.com'],
        fail_silently=False,
    )
    cache.delete(s_date)
