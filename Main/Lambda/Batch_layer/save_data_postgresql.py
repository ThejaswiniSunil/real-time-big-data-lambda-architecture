from sqlalchemy import create_engine
from config import PG_URL


def save_data(data):
    engine = create_engine(PG_URL)
    data.to_sql('Phone', engine, if_exists='replace', index=False)
    print("data stored in postgresql")
