from flask import Flask, request, jsonify
from firestore import *
from selectors import *

app = Flask(__name__)


@app.route('/item_name', methods=['POST'])
def post():
    item_name = str(request.data.get('item_name', ''))
    zip_code = str(request.data.get('zip_code', ''))


def perform_search(item_name, quantity, zip_code='90024', store='walmart'):
    product_list = searchWithIds(item_name, quantity, zip_code, store)
    for product in product_list:
        add_item("items", item_name, product, quantity)


if __name__ == '__main__':
    app.run(debug=True)
