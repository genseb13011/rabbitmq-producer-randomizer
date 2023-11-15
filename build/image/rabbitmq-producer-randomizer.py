#!/usr/bin/env python
import pika, random, time, os 
 
#variables 
rabbitmq_user=os.environ.get('RABBITMQ_USER') 
rabbitmq_password=os.environ.get('RABBITMQ_PASSWORD') 
rabbitmq_url=os.environ.get('RABBITMQ_URL') 
rabbitmq_port=os.environ.get('RABBITMQ_PORT') 
rabbitmq_vhost=os.environ.get('RABBITMQ_VHOST') 
rabbitmq_exchange=os.environ.get('RABBITMQ_EXCHANGE') 
random_message_routing_key=os.environ.get('RANDOM_MESSAGE_ROUTING_KEY') 
random_message_length_min=int(os.environ.get('RANDOM_MESSAGE_LENGTH_MIN')) 
random_message_length_max=int(os.environ.get('RANDOM_MESSAGE_LENGTH_MAX')) 
random_message_characters=os.environ.get('RANDOM_MESSAGE_CHARACTERS') 
message_generation_milliseconds=int(os.environ.get('MESSAGE_GENERATION_MILLISECONDS')) 
messages_to_process_before_closing_connection=int(os.environ.get('MESSAGES_TO_PROCESS_BEFORE_CLOSING_CONNECTION')) 
 
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)  
 
infinite_loop = True 
while (infinite_loop): 
    random_message_count=0 
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_url,rabbitmq_port,rabbitmq_vhost,credentials)) 
    channel = connection.channel() 
    while random_message_count <= messages_to_process_before_closing_connection: 
        message_length = random.randrange(random_message_length_min, random_message_length_max) 
        message_body = ''.join(random.choice(random_message_characters) for i in range (message_length))  
        channel.basic_publish(exchange=rabbitmq_exchange, 
                              routing_key=random_message_routing_key, 
                              body=message_body) 
 
        time.sleep(message_generation_milliseconds/1000) 
        print(" [x] Message %s sent" % (message_body)) 
 
        random_message_count = random_message_count + 1

    connection.close()
    print("Connection closed")
