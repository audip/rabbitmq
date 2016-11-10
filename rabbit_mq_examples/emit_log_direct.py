#!/usr/bin/env python
import pika 
import sys
import random
import time

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create exchange
channel.exchange_declare(exchange='direct_logs', type='direct')

# publish message to queue
severities = ['info','warning','error']
for _ in range(50):
    severity = random.choice(severities)
    message = 'logging ' + severity
    channel.basic_publish(exchange='direct_logs',
                          routing_key=severity,
                          body=message)
    print "Sent %r: %r" % (severity, message)
    time.sleep(random.randint(1, 10))

# close connection
connection.close()
