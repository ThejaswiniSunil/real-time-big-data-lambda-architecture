# Simple scheduler standing in for the Airflow DAG: run the batch layer every 60 s.
import os
import time
from Batch_layer.batch_layer import batch_layer

while True:
    try:
        batch_layer()
    except Exception as e:
        print(f"Batch run skipped/failed (no data yet?): {str(e)[:200]}")
    time.sleep(int(os.getenv("BATCH_INTERVAL", "60")))
