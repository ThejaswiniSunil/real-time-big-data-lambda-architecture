import ast
import pickle
from config import MODEL_PATH

BRANDS = ['Maxfone', 'Infinix', 'Freeyond', 'XIAOMI', 'Tecno', 'Oppo', 'Nokia',
          'Samsung', 'Huawei', 'Vivo', 'Realme', 'Sowhat', 'Apple']
SIMS = ['Dual', 'Single']


def map_brand_to_numeric(brand):
    return BRANDS.index(brand) + 1 if brand in BRANDS else 14


def map_sim_type_to_numeric(sim_type):
    return SIMS.index(sim_type) + 1 if sim_type in SIMS else 3


def map_numeric_to_brand(number):
    number = int(number)
    return BRANDS[number - 1] if 1 <= number <= len(BRANDS) else 'Unknown'


def map_numeric_to_sim_type(number):
    number = int(number)
    return SIMS[number - 1] if 1 <= number <= len(SIMS) else 'Unknown'


_model = None


def get_model():
    global _model
    if _model is None:
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
    return _model


def transformation(original_list):
    """original_list: a CSV row (as its str() from Kafka) -> [brand, screen, ram, rom, sim, battery, price]"""
    row = ast.literal_eval(original_list)
    features = [
        map_brand_to_numeric(row[1]),
        float(row[3]),   # screen size
        float(row[4]),   # RAM
        float(row[5]),   # storage
        map_sim_type_to_numeric(row[7]),
        float(row[8]),   # battery
    ]
    price = float(get_model().predict([features])[0])
    return [map_numeric_to_brand(features[0]), features[1], features[2], features[3],
            map_numeric_to_sim_type(features[4]), features[5], price]
