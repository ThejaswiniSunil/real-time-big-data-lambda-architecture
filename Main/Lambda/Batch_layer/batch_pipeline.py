# Consumer-only: the producer already runs in the stream service.
import time
from HDFS_consumer import consum_hdfs

while True:
    try:
        consum_hdfs()
    except Exception as e:
        print(f"Error in HDFS consumer: {e}")
    time.sleep(3)
