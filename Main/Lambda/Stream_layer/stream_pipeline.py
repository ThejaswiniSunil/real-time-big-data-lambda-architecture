import threading
import time
from config import STREAM_CSV
from producer import send_message
from Stream_layer.ML_consumer import consum
from Stream_data.stream_data import generate_real_time_data


def producer_loop():
    while True:
        try:
            send_message(generate_real_time_data(STREAM_CSV))
            time.sleep(5)
        except Exception as e:
            print(f"Error in producer: {e}")
            time.sleep(5)


def consumer_loop():
    while True:
        try:
            consum()
        except Exception as e:
            print(f"Error in consumer: {e}")
        time.sleep(3)


threading.Thread(target=producer_loop, daemon=True).start()
consumer_loop()
