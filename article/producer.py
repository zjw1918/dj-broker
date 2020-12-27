import pika, random
params = pika.URLParameters('amqps://hlljmpie:Rma05njTX6PhxEMLZe4YWNQpL-iCK09n@gerbil.rmq.cloudamqp.com/hlljmpie')

conn = pika.BlockingConnection(params)
channel = conn.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='helllo {}'.format(random.randint(0, 100)))

if __name__ == "__main__":
    publish()

