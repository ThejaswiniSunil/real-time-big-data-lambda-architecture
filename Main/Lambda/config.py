import os
TOPIC = "smartphoneTopic"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
HBASE_HOST = os.getenv("HBASE_HOST", "localhost")
HDFS_URL = os.getenv("HDFS_URL", "http://localhost:9870")        # WebHDFS
HDFS_NN = os.getenv("HDFS_NN", "hdfs://localhost:9000")          # Spark
HDFS_USER = os.getenv("HDFS_USER", "root")
RAW_DIR = "/batch-layer/raw"
PG_URL = os.getenv("PG_URL", "postgresql://postgres:postgres@localhost:5433/bigdata")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STREAM_CSV = os.path.join(BASE_DIR, "Stream_data", "stream_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "ML_operations", "xgb_model.pkl")
