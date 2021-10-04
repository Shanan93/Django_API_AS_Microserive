import pika, json

params = pika.URLParameters('amqps://bsxpusqs:rv66FF1gv24ub566F3xducMmGH4BLuco@cattle.rmq2.cloudamqp.com/bsxpusqs')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)