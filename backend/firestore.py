import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from selector import searchWithIds

list_of_items = [
    'apples',
    'beverages',
    'bread',
    'cheese',
    'chips',
    'coca cola',
    'condiments',
    'egg',
    'flour',
    'frozen food',
    'juice',
    'lemon',
    'milk',
    'oranges',
    'pizzas',
    'prepared food'
]

list_of_market = [
    'target',
    'cvs'
]

num_item = 5

class firebaseAPI:
    def __init__(self):
        # Use a service account
        cred = credentials.Certificate('seek-525ee-2cc702803f50.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def store(self, col, cat, data=[]):
        doc_ref = self.db.collection(u"{}".format(col)).document(u"{}".format(cat))
        i = 5
        for d in data:
            if (len(d['address']) > 0 and len(d['availability'])>0 and len(d['distance'])>0):
                doc_ref.set({
                    "{}".format(i): d},
                    merge=True
                )
                i = i + 1


db = firebaseAPI()
postcode = list(db.db.collection(u'users').document(u'postcode').get().to_dict().values())

for item in list_of_items:
    for postcode in postcode:
        for market in list_of_market:
            print("scraping {0} at {1} with postcode {2}".format(item, market, postcode))
            data = searchWithIds(item, num_item, postcode, market)
            db.store("items", item, data)

