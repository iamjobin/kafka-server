from kafka import KafkaProducer
import json
import time

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(5):
    message = {"id": i, "text": f"Hello Kafka {i}"}
    producer.send("demo-topic", message)
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()   # ensure all messages sent
producer.close()
