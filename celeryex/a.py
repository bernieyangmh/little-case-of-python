import time
from celery.task import task


@task
def say(x,y):
        time.sleep(10)
        return x+y

