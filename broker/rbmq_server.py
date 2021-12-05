# worker.py
import pika
import pickle


class RabbitServer(object):
    def __init__(self, host="localhost", port=5672, queue=None):
        credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host, port=port, credentials=credentials, virtual_host='vhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue, durable=True)

        self.channel.basic_consume(on_message_callback=self.callback, queue=queue, auto_ack=True)
        self.dispatcher = RpcMethodDispatcher()
        self.setup = self.dispatcher.setup

    def callback(self, ch, method, properties, body):
        body = pickle.loads(body)
        print(body)

        func = self.dispatcher.dispatch(body.get("method"))
        if not func:
            return
        try:
            func(**body.get("data"))
        except Exception as e:
            print(e)

    def run(self):
        print("wait")
        self.channel.start_consuming()


class RpcMethodDispatcher(object):
    def __init__(self):
        self.map = []

    def setup(self, name):
        # 和message中的method相互对应类似于@app.route("/")，将所有路由添加过来
        def deco(f):
            self.map.append(MethodMap(name, f))

            def wrapper(*args, **kwargs):
                return f(*args, **kwargs)

            return wrapper

        return deco

    def dispatch(self, name):
        for i in self.map:
            if i.name == name:
                return i.method


class MethodMap(object):
    def __init__(self, name, method):
        self.name = name
        self.method = method


server = RabbitServer(queue="task_queue")

if __name__ == '__main__':
    server.run()
