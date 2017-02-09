import sys
from celery import Celery

app = Celery()

app.config_from_object('celeryconfig')
app.send_task("a.say",[sys.argv[1],sys.argv[2]])