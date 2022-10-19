import json
from saleapp import app


def load_categories():
    with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)

def load_products():
   with open('%s/data/products.json' % app.root_path, encoding= 'utf-8') as f:
       return json.load(f)