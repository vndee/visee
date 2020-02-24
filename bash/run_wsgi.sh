#!/usr/bin/env bash
export PYTHONPATH=/visee
cd /visee/rest/
gunicorn --bind 0.0.0.0:8000 endpoint:app