import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from config import HDFS_NN, RAW_DIR
from transform import map_brand_to_numeric, map_sim_type_to_numeric, get_model

NUMERIC = ["screen_size", "ram", "rom", "battary"]


def get_spark():
    return (SparkSession.builder.master("local[*]").appName("batch-layer")
            .config("spark.driver.memory", "1g").getOrCreate())


def spark_tranform():
    spark = get_spark()
    df = (spark.read.option("header", True).option("escape", '"')
          .csv(f"{HDFS_NN}{RAW_DIR}/"))
    for c in NUMERIC:
        df = df.withColumn(c, F.col(c).cast("float"))
    df = df.dropna(subset=NUMERIC + ["brand", "sim_type"])

    pdf = df.toPandas()                      # small data: predict on the driver with the XGBoost model
    features = pd.DataFrame({
        "brand": pdf["brand"].map(map_brand_to_numeric),
        "screen_size": pdf["screen_size"],
        "ram": pdf["ram"],
        "rom": pdf["rom"],
        "sim_type": pdf["sim_type"].map(map_sim_type_to_numeric),
        "battary": pdf["battary"],
    })
    pdf["price"] = get_model().predict(features)
    print(f"data transformed successfully: {len(pdf)} rows")
    return pdf
