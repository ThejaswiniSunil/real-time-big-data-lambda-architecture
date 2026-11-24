from kafka import KafkaConsumer
from config import KAFKA_BOOTSTRAP, TOPIC
from transform import transformation
from Stream_layer.insert_data_hbase import insert_dataHbase


def consum():
    consumer = KafkaConsumer(TOPIC,
                             group_id='ml_stream_group',          # distinct from the HDFS consumer's group
                             auto_offset_reset='latest',
                             bootstrap_servers=KAFKA_BOOTSTRAP,
                             value_deserializer=lambda x: x.decode('utf-8'))
    for message in consumer:
        try:
            res = transformation(message.value)
            insert_dataHbase(res)
        except Exception as e:
            print(f"Error processing message: {e}")
