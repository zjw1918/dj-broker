import pika
params = pika.URLParameters('amqps://**@gerbil.rmq.cloudamqp.com/hlljmpie')

conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('receive <<<' + str(body))    

channel.basic_consume(queue='admin', on_message_callback=callback)
print('start consuming...')
channel.start_consuming()
channel.close()

