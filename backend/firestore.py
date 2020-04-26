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


lis = [{'imageUrl': 'https://i5.walmartimages.com/asr/f9dd906b-38e0-4f63-a599-99d96d383f85_1.148a9bedcbcd7624715ffb8038fa36a3.jpeg', 'address': [], 'availability': [], 'distance': [], 'price': [48.0, 68.9, 399.0, 749.0, 24.8, 28.8, 1.0, 7.1, 5.0, 32.8, 41.6, 68.9, 209.0, 258.9, 10.5, 9.8, 398.0, 497.0, 698.0, 998.0, 199.0, 279.0, 57.8, 56.9, 279.0, 508.9, 10.8, 2.0, 48.0, 68.9, 249.0, 308.9, 32.8, 68.9, 118.0, 228.0]}, {'imageUrl': 'https://i5.walmartimages.com/asr/64a81ebf-8f5a-4f43-b6c9-9aca178a580e_2.a4229da3e26ab3488c9e27421bdedcac.jpeg', 'address': ['5450 New Hope Commons DrDurham NC 27707', '501 Hampton Pointe BHillsborough NC 27278', '1001 Shiloh Glenn DrMorrisville NC 27560', '3560 Davis DrMorrisville NC 27560', '2750 Nc 55 HwyCary NC 27519', '1318 Mebane Oaks RdMebane NC 27302', '2010 Kildaire Farm RdCary NC 27518', '3151 Apex PeakwayApex NC 27502', '1525 Glenn School RdDurham NC 27704', '10050 Glenwood AveRaleigh NC 27617', '12500 Us 15 501 NChapel Hill NC 27517', '973 N Harrison AveCary NC 27513', '6600 Glenwood AveRaleigh NC 27612', '1725 New Hope Church RdRaleigh NC 27609', '8000 Town Dr.Raleigh NC 27616', '2114 S Main StWake Forest NC 27587', '4500 Fayetteville RdRaleigh NC 27603', '4431 New Bern AveRaleigh NC 27610'], 'availability': [True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False], 'distance': ['4.22', '8.69', '10.72', '13.76', '15.33', '18.81', '20.33', '20.5', '6.12', '11.22', '12.28', '16.37', '16.43', '22.06', '23.18', '23.28', '25.19', '25.63'], 'price': [8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8, 8.8]}, {'imageUrl': 'https://i5.walmartimages.com/asr/aa377b3b-735c-481b-9842-cf699ea8f088_1.fb67f2e8989ff2c48a776f3087582035.png',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'address': ['5450 New Hope Commons DrDurham NC 27707', '1525 Glenn School RdDurham NC 27704', '12500 Us 15 53', '1725 New Hope Church RdRaleigh NC 27609', '3151 Apex PeakwayApex NC 27502', '8000 Town Dr.Raleigh NC 27616', '2114 S Main StWake Forest NC 27587', '10050 Glenwood AveRaleigh NC 27617', '501 Hampton Pointe BHillsborough NC 27278', '1318 Mebane Oaks RdMebane NC 27302', '2010 Kildaire Farm RdCary NC 27518', '4500 Fayetteville RdRaleigh NC 27603', '4431 New Bern AveRaleigh NC 27610'], 'availability': [True, True, True, True, True, True, True, False, True, False, False, False, False, False, False, False], 'distance': ['4.7', '5.5', '12.7', '13.5', '15.2', '16', '21.5', '20.3', '22.5', '22.6', '10.6', '9.3', '19.5', '20', '24.8', '25.1'], 'price': [18.7, 18.7, 18.7, 18.7, 18.7, 18.7, 18.7, 18.7, 18.7, 18.7, 11.1, 18.7, 18.7, 18.7, 18.7, 18.7]}, {'imageUrl': 'https://i5.walmartimages.com/asr/75097901-36c0-4425-88f2-f23380c403be_1.ea2b299100486bb40b250539541f0a1c.jpeg', 'address': [], 'availability': [], 'distance': [], 'price': [99.0, 139.0, 26.4, 33.4, 64.0, 138.6, 1.9, 10.8, 58.4, 68.9, 8.0, 21.4, 24.8, 28.8, 1.0, 11.4, 23.2, 23.9, 5.0, 7.0, 16.8, 11.4, 8.0, 21.3, 7.8, 5.8, 10.7, 36.2, 15.8, 18.7, 55.6, 73.9, 5.0, 32.7, 220.0, 284.0]}, {'imageUrl': 'https://i5.walmartimages.com/asr/2ea4b7b3-0af2-4dea-821c-78da476c2cbc_1.18835d5649f666d381161784b9179e55.jpeg', 'address': [], 'availability': [], 'distance': [], 'price': [199.0, 299.0, 2.5, 1.0, 17.7, 18.5, 26.4, 28.9, 14.7, 16.4, 48.7, 58.9, 42.8, 35.0, 47.2, 68.9, 219.0, 236.9, 19.8, 34.5, 49.8, 56.7, 7.4, 7.2, 5.0, 17.1, 149.0, 169.0, 11.7, 16.8, 25.0, 58.7, 28.8, 33.8, 20.7, 21.7]}]
name = 'items'
index = 0
for item in lis:
    add_item('items', 'milk', item, index)
    index = index + 1
