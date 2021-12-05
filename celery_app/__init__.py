from celery import Celery

app = Celery('demo', broker='amqp://celery:celery@broker:5672/vhost')
app.config_from_object('celery_app.celery_config')