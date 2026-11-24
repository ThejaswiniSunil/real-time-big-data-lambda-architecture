from kafka import KafkaProducer
from config import KAFKA_BOOTSTRAP, TOPIC

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP)


def send_message(message):
    try:
        producer.send(TOPIC, str(message).encode('utf-8'))
        print(f"Produced: {str(message)[:80]}... to Kafka topic: {TOPIC}")
    except Exception as error:
        print(f"Error: {error}")
