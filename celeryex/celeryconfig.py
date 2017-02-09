CELERY_IMPORTS = ('a')
CELERY_IGNORE_RESULT = False
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 5672
BROKER_URL = 'amqp://'
# 使用amqp消息队列
#CELERY_RESULT_BACKEND = 'amqp'

# 使用mongodb
CELERY_RESULT_BACKEND = 'mongodb'
CELERY_RESULT_BACKEND_SETTINGS = {
        "host":"127.0.0.1",
        "port":27017,
        "database":"fun",
        "taskmeta_collection":"stock_taskmeta_collection",
}

#celery worker -l info --beat  启动命令