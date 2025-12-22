import json
import uuid
from confluent_kafka import Producer

# Kafka producer configuration tell where to find Kafka brokers advertised to clients that want to produce send events to Kafka topics
ProducerConfig = Producer({
    'bootstrap.servers': 'localhost:9092'
})
# callback function to handle delivery reports
def delivery_report(err, msg):
    if err :     
        print(f"Message delivery failed: {err}")
    else:   
        print(f"Message delivered to {msg.value().decode('utf-8')} ")
#expect an event structure for an order
        print(dir(msg))
        #show topic name partition and offset where the message is stored
        print(f"Message delivered to {msg.value().decode('utf-8')} on Topic: {msg.topic()}, Partition: {msg.partition()}, Offset: {msg.offset()}")
#exple of event to be sent to Kafka topic
event = {
    'order_id': str(uuid.uuid4()),
    'customer_id': str(uuid.uuid4()),
    'customer_name': 'Mohamed Amine Blibech',
    'item_name': 'pizza nuptine large',
    'quantity': 2
}

#convert this objet data type to json string before sending it to Kafka topic
value=json.dumps(event).encode('utf-8')

#send event to Kafka topic named 'orders'
ProducerConfig.produce(topic='orders', value=value,
                       #troubleshooting callback function to handle delivery reports
                       callback=delivery_report
                       )

#flush the producer to ensure all messages are sent before exiting
ProducerConfig.flush()