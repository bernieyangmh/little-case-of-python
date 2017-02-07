"""
mac下配置rabbitmq：http://blog.csdn.net/a355586533/article/details/51802195


一个终端A：celery -A celeryeg worker --loglevel=info
一个终端B:启动python，调用say
函数say立刻执行，5s后在A显示say的结果
"""
import time
from celery import Celery

app = Celery('celeryeg',broker='amqp://guest@localhost//')

@app.task
def say(x,y):
    time.sleep(5)
    return x+y

if __name__ == '__main__':
    say('Hello','World')

