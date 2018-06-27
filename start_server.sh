#!/usr/bin/env bash

source /home/vibloteam/timit_env/bin/activate
cd /home/vibloteam/Project/tabby_search
gunicorn tabby_search.wsgi --daemon
python manage.py start_cached_model