#!/usr/bin/env bash
export PYTHONPATH=/visee
cd /visee/rest/
gunicorn endpoint:app