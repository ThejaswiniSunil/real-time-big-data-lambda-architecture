import time
import uuid
import pandas as pd
from hdfs import InsecureClient
from config import HDFS_URL, HDFS_USER, RAW_DIR

COLUMNS = ['id', 'brand', 'model_name', 'screen_size', 'ram', 'rom', 'cams', 'sim_type', 'battary',
           'sale_percentage', 'product_rating', 'seller_name', 'seller_score', 'seller_followers', 'Reviews']

client = InsecureClient(HDFS_URL, user=HDFS_USER)


def store_data_in_hdfs(record):
    """Each Kafka record becomes its own small CSV in HDFS (avoids single-datanode append problems)."""
    csv_text = pd.DataFrame([record], columns=COLUMNS).to_csv(index=False)
    client.makedirs(RAW_DIR)
    path = f"{RAW_DIR}/{int(time.time() * 1000)}-{uuid.uuid4().hex[:8]}.csv"
    client.write(path, data=csv_text, encoding='utf-8')
    print("Stored in HDFS:", path)
