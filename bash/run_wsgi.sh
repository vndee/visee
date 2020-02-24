#!/usr/bin/env bash
export PYTHONPATH=/visee
cd /visee/rest/
gunicorn --bind visee_rest:8000 endpoint:app