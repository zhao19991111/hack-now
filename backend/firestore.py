import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/minjingshi/.kube/tokens.json"

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

# seek-2222
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'seek-525ee',
})

db = firestore.client()


def add_item(name, doc, data, index):
    docref = db.collection(name).document(
        doc)

    docref.set({
        u'{}'.format(index): data
    }, merge=True)


def add_item_sub(name, doc, data, ref):

    subref = ref.collection(u'{}'.format(name)).document(u'{}'.format(doc))
    subref.set(u'{}'.format(data))


def retrieve_item(name, doc):
    docref = db.collection(u'{}'.format(name)).document(u'{}'.format(doc))
    list_of_items = []
    for doc in docref:
        list_of_items.append(doc.data())
