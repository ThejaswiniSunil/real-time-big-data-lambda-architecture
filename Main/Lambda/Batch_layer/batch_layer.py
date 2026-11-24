from spark_tranformation import spark_tranform
from save_data_postgresql import save_data


def batch_layer():
    save_data(spark_tranform())
