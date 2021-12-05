#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')

connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost', port=5672, credentials=credentials, virtual_host='vhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, propertites, body):
    print(" [x] Received {}".format(body))


channel.basic_consume('hello', callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()