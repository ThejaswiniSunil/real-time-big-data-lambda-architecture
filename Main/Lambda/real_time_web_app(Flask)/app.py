from flask import Flask, render_template
from get_Data_from_hbase import get_last_record_from_hbase

app = Flask(__name__)


@app.route('/')
def index():
    try:
        last_record = get_last_record_from_hbase()
    except Exception as e:
        print(f"HBase not ready: {e}")
        last_record = {}
    return render_template('index.html', last_record=last_record)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
