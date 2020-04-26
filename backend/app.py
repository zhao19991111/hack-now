from flask import Flask, request, jsonify
from firestore import *
from selector import *

app = Flask(__name__)

list_of_market = [
    'target',
    'cvs'
]


@app.route('/item_name', methods=['POST'])
def post():
    item_name = str(request.data.get('item_name', ''))
    zip_code = str(request.data.get('zip_code', ''))
    perform_search(item_name, 5, zip_code, list_of_market)


def perform_search(item_name, quantity=5, zip_code='90024', store=[]):
    for st in store:
        product_list = searchWithIds(item_name, quantity, zip_code, store)
        for product in product_list:
            db.store('items', item_name, product)


if __name__ == '__main__':
    app.run(debug=True)
