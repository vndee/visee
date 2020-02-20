#!/usr/bin/env bash
export PYTHONPATH=$PWD
cd rest/
gunicorn endpoint:app