from firestore import *
from selector import *


def perform_search(item_name, quantity, zip_code='90024', store='walmart'):
    product_list = searchWithIds(item_name, quantity, zip_code, store)
    for product in product_list:
        add_item("item", item_name, product)


perform_search('milk', 3)
