FROM alpine:3.18.4
RUN apk add python3 py3-pip
RUN pip3 install pika
RUN mkdir /opt/rabbitmq-producer-randomizer
COPY rabbitmq-producer-randomizer.py /opt/rabbitmq-producer-randomizer
RUN chmod +x /opt/rabbitmq-producer-randomizer/rabbitmq-producer-randomizer.py
CMD /opt/rabbitmq-producer-randomizer/rabbitmq-producer-randomizer.py
