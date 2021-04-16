celery -A backend.celery worker --loglevel=info --detach && \ 
newrelic-admin run-program gunicorn --bind 0.0.0.0:8000 backend.wsgi