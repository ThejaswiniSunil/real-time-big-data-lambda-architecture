import happybase
from config import HBASE_HOST


def decode_dict(d):
    return {k.decode('utf-8').split(':', 1)[1]: v.decode('utf-8') for k, v in d.items()}


def get_last_record_from_hbase():
    connection = happybase.Connection(HBASE_HOST)
    try:
        if b'smartphone' not in connection.tables():
            return {}
        table = connection.table('smartphone')
        for _, data in table.scan(limit=1, reverse=True):
            return decode_dict(data)
        return {}
    finally:
        connection.close()
