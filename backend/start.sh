#!/bin/bash  
newrelic-admin run-program gunicorn --bind 0.0.0.0:8000 backend.wsgi