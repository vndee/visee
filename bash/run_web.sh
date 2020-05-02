#!/usr/bin/env bash
export PYTHONPATH=/visee
cd /visee/web/
gunicorn --bind visee_web:8888 django_visee.wsgi