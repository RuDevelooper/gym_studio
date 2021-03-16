#!/bin/bash
source /home/master/code/gymstudio/venv/bin/activate
exec gunicorn  -c "/home/master/code/gymstudio/gunicorn_config.py" gymstudio.wsgi