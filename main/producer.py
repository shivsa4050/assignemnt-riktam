#amqps://kcygnlqo:q-iNbJdpsQPgiL5XbaEDPEUcec5jihXk@puffin.rmq2.cloudamqp.com/kcygnlqo
import pika, json
params=pika.URLParameters('amqps://kcygnlqo:q-iNbJdpsQPgiL5XbaEDPEUcec5jihXk@puffin.rmq2.cloudamqp.com/kcygnlqo')
connection=pika.BlockingConnection(params)
channel=connection.channel()

def publish(method,body):
    properties= pika.BasicProperties(method)
    print("Inside Publisher")
    channel.basic_publish(exchange='',routing_key='admin',body=json.dumps(body),properties=properties)

