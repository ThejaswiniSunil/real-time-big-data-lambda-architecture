import ast
from kafka import KafkaConsumer
from config import KAFKA_BOOTSTRAP, TOPIC
from put_data_hdfs import store_data_in_hdfs


def consum_hdfs():
    consumer = KafkaConsumer(TOPIC,
                             group_id='hdfs_batch_group',         # distinct group so both layers see every message
                             auto_offset_reset='latest',
                             bootstrap_servers=KAFKA_BOOTSTRAP,
                             value_deserializer=lambda x: x.decode('utf-8'))
    for message in consumer:
        try:
            store_data_in_hdfs(ast.literal_eval(message.value))
        except Exception as e:
            print(f"Error storing message in HDFS: {e}")
