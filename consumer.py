import json
from confluent_kafka import Consumer
# Kafka consumer configuration to connect to Kafka brokers and subscribe to topics
ConsumerConfig = Consumer({
    'bootstrap.servers': 'localhost:9092',
    # Consumer group ID for coordinating message consumption
    'group.id': 'order-consumers',
    # Automatically reset the offset to the earliest message if no offset is found for the consumer group 
    'auto.offset.reset': 'earliest'
})
#subscribe to the 'orders' topic to consume messages
ConsumerConfig.subscribe(['orders'])
print("Consumer is listening to 'orders' topic...")
try:
        #poll for new messages from the topic
        while True:
            msg = ConsumerConfig.poll(1.0)  # timeout set to 1 second
            if msg is None:
                continue  # no message received, continue polling
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            #process the received message
            value = msg.value().decode('utf-8')
            #convert the json string back to a Python object
            orders = json.loads(value)
            #display the received order
            print(f"Received order: {orders['quantity']} x {orders['item_name']} for {orders['customer_name']} (Order ID: {orders['order_id']})")  

except KeyboardInterrupt:
    pass
finally:
    #close the consumer to release resources
    ConsumerConfig.close()  