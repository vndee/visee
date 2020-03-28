#!/usr/bin/env bash
export PYTHONPATH=/visee
cd /visee/web/
gunicorn django_visee.wsgi