import pika, json
from main import Product,db

params=pika.URLParameters('amqps://kcygnlqo:q-iNbJdpsQPgiL5XbaEDPEUcec5jihXk@puffin.rmq2.cloudamqp.com/kcygnlqo')
connection=pika.BlockingConnection(params)
channel=connection.channel()
channel.queue_declare(queue='main')


def callback(ch,method,properties,body):
    print("Main RECIEVED")
    data= json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        print(properties.content_type)
        product=Product(id=data['id'],title=data['title'],chat=data['chat'])
        db.session.add(product)
        db.session.commit()

    elif properties.content_type == 'product_updated':
        print(properties.content_type)
        product=Product.query.get(data['id'])
        product.title=data['title']
        product.chat=data['chat']
        db.session.commit()

    elif properties.content_type == 'product_deleted':
        print(properties.content_type)
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()




channel.basic_consume(queue='main',on_message_callback=callback,auto_ack=True)
print("Started Consuming")
channel.start_consuming()
channel.close()