from firebase import firebaseAPI

config = {"apiKey": "AIzaSyDZPaKcPaC0xnoxM1qYsUPEbuON1krqlP4", "authDomain": "seek-525ee.firebaseapp.com", "databaseURL": "https://seek-525ee.firebaseio.com", "projectId": "seek-525ee", "storageBucket": "seek-525ee.appspot.com", "messagingSenderId": "803806872501", "appId": "1:803806872501:web:ce8936ff30475b2bed4ffc", "measurementId": "G-2FWD6N6E9V"}

item = firebaseAPI(config)

item.store_data("item", 6, ["apple", "qty"])
