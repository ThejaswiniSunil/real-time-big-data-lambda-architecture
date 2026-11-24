from datetime import datetime
import happybase
from config import HBASE_HOST


def insert_dataHbase(data):
    connection = happybase.Connection(HBASE_HOST)
    try:
        if b'smartphone' not in connection.tables():
            connection.create_table('smartphone', {'info': dict()})
        table = connection.table('smartphone')
        now = datetime.now()
        table.put(now.strftime('%Y%m%d%H%M%S%f').encode(), {
            b'info:date': now.strftime('%Y-%m-%d %H:%M:%S').encode(),
            b'info:Brand': str(data[0]).encode(),
            b'info:Screen_size': str(data[1]).encode(),
            b'info:RAM': str(data[2]).encode(),
            b'info:Storage': str(data[3]).encode(),
            b'info:Sim_type': str(data[4]).encode(),
            b'info:Battery': str(data[5]).encode(),
            b'info:Price': str(round(data[6], 2)).encode(),
        })
        print("Data inserted into HBase: ", data)
    finally:
        connection.close()
