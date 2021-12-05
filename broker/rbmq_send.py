#!/usr/bin/env python
import pika
import pickle

def test_func():
    print('hi')

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')

connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost', port=5672, credentials=credentials, virtual_host='vhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=test_func.__str__())
print(" [x] Sent 'Hello World!'")
connection.close()


