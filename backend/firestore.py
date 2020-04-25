import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import selector

class firebaseAPI:
    def __init__(self):
        # Use a service account
        cred = credentials.Certificate('seek-525ee-2cc702803f50.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def store(self, col, cat, data={}):
        doc_ref = self.db.collection(u"{}".format(col)).document(u"{}".format(cat))
        doc_ref.set({
            u"{}".format(cat): data,
        })

data = [{'imageUrl': 'https://i5.walmartimages.com/asr/11cddf33-e7d7-4946-9580-578d7136a0a7_1.8e96101312ffe08a9d74f2709255173c.jpeg', 'address': [], 'availability': [], 'distance': [], 'price': [75.0, 95.0, 8.0, 23.9, 27.8, 40.7, 25.7, 33.7, 40.7, 68.9, 47.2, 58.5, 15.0, 65.8, 32.8, 68.9, 9.0, 43.7, 7.8, 20.9, 1.0, 12.7, 1.0, 48.9, 9.7, 12.1, 58.4, 68.9, 268.0, 608.9, 318.0, 398.0, \
27.8, 48.9, 5.0, 13.0]}, {'imageUrl': 'https://i5.walmartimages.com/asr/ecf7636f-2cf7-4068-b9c3-609ddb843311_1.3d6c15cd9c1c68d3df7697f06ef03370.jpeg', 'address': [], 'availability': [], 'distance': [], 'price': [17.7, 58.9, 43.6, 48.9, 0.3, 68.9, 7.4, \
5.1, 21.0, 107.8, 9.0, 43.7, 7.0, 15.7, 89.0, 128.5, 159.0, 308.9, 18.8, 37.9, 658.0, 998.0, 47.2, 58.5, 24.2, 28.9, 27.7, 43.9, 21.7, 21.9, 10.2, 11.8, 128.0, 138.0, 2.5, 7.8]}, {'imageUrl': 'https://i5.walmartimages.com/asr/45c706f8-785a-4fd2-895b-79ce82652f0c_1.2d0c2592b92ba9e58e3b60ce27df973b.jpeg', 'address': [], 'availability': [], 'distance': [], 'price': [37.3, 58.4, \
27.7, 30.6, 40.8, 34.6, 41.6, 48.9, 99.0, 118.0, 50.7, 58.7, 10.2, 11.8, 349.0, 398.0, 97.0, 118.9, 98.5, 98.6, 119.0, 158.9, \
24.2, 30.0, 24.7, 22.4, 17.7, 18.5, 38.7, 58.9, 244.0, 338.9, 20.7, 39.2, 21.0, 38.8]}, {'imageUrl': 'https://i5.walmartimages.com/asr/4213ec5e-b259-4378-bcd4-d26ad8b3f33c_1.06909905f75d664ba8ff1384c6a1ddfa.jpeg', 'address': ['8333 Van Nuys BlvdPanorama City CA 91402', '14441 Inglewood AveHawthorne CA 90250', '14530 Nordhoff StPanorama City CA 91402', '6433 Fallbrook AveWest \
Hills CA 91307', '9001 Apollo WayDowney CA 90242', '19503 Normandie AveTorrance CA 90501', '19821 Rinaldi StPorter Ranch CA 91326', '4651 Firestone BlvdSouth Gate CA 90280', '22015 Hawthorne BlvdTorrance CA 90503', '2100 N Long Beach BlvdCompton CA 90221', '8500 Washington BlvdPico Rivera CA 90660'], 'availability': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False], 'distance': ['11.2', '12', '12', '13.7', '13.9', '16.3', '16.6', '16.3', '16.9', '17', '20', '20.2', '20.4', '21.3', '19.2', '11', '15.1', '17.9', '21.8', '22.7', '22.8'], 'price': [20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4, 20.4]}, {'imageUrl': 'https://i5.walmartimages.com/asr/a014d1ab-cba2-40a5-80b7-acf47683038f_1.828ee50e8be8659d84a261e8ffe80eb7.jpeg', 'address': [], 'availability': [], 'distance': [], 'price': [21.0, 35.8, 3.3, 11.8, 9.0, 40.0, 74.0, 148.0, 1.0, 14.4, 17.0, 32.8, 17.6, 23.6, 23.6, 33.6, 618.0, 1008.9, 44.0, 79.0, 58.4, 68.9, 79.0, 208.5, 11.8, 42.3, 48.0, 68.9, 399.0, 499.0, 
69.0, 79.0, 220.0, 284.0, 14.7, 16.4]}]

db = firebaseAPI()
db.store("items", "milk", data)

