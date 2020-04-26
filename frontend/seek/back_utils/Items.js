import * as firebase from "firebase";
import axios from "axios";
const stringSimilarity = require("string-similarity");

class Items {
  constructor() {
    // Your web app's Firebase configuration
    var firebaseConfig = {
      apiKey: "AIzaSyDZPaKcPaC0xnoxM1qYsUPEbuON1krqlP4",
      authDomain: "seek-525ee.firebaseapp.com",
      databaseURL: "https://seek-525ee.firebaseio.com",
      projectId: "seek-525ee",
      storageBucket: "seek-525ee.appspot.com",
      messagingSenderId: "803806872501",
      appId: "1:803806872501:web:ce8936ff30475b2bed4ffc",
      measurementId: "G-2FWD6N6E9V"
    };
    if (!firebase.apps.length) {
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);
      firebase.analytics();
    }
    // fire store
    this.db = firebase.firestore();
  }

  async loadAllMatch(name) {
    const snapshot = await this.db.collection("items").get();

    let data_arr = {};
    snapshot.docs.map((doc) => {
      data_arr[doc.id] = Object.values(doc.data());
    });
    let all_item_names = Object.keys(data_arr);

    let result_arr = [];
    let best_matches = this.findKBestMatches(name, all_item_names, 3);
    console.log(best_matches);
    for (let match of best_matches) {
      result_arr = result_arr.concat(data_arr[match]);
    }
    console.log(result_arr);
    return result_arr;
  }

  findKBestMatches(target, source, num_matches = 1) {
    let result = [];
    let source_set = new Set(source);

    for (let i = 0; i < num_matches; i++) {
      let best_match = stringSimilarity.findBestMatch(
        target,
        Array.from(source_set)
      );
      result.push(best_match.bestMatch.target);
      source_set.delete(best_match.bestMatch.target);
    }

    return result;
  }

  addItemToCart(itemObj) {
    this.db
      .collection("favorite")
      .add(itemObj)
      .then(() => {
        return itemObj;
      });
  }

  async getAllItemsFromCart() {
    const snapshot = await this.db.collection("favorite").get();
    let data_arr = [];
    snapshot.docs.map((doc) => {
      data_arr.push(doc.data());
    });
    return data_arr;
  }
}

export { Items };
