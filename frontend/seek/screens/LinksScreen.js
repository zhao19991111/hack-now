import * as WebBrowser from "expo-web-browser";
import * as React from "react";
import { StyleSheet, Text, View } from "react-native";
import { RectButton, ScrollView } from "react-native-gesture-handler";
import ItemCard from "../components/ItemCard.js";
import { Items } from "../back_utils/Items.js";
import { Button, SearchBar } from "react-native-elements";
import { Ionicons, AntDesign } from "@expo/vector-icons";
import axios from "axios";

import Geolocation from "@react-native-community/geolocation";

export default function LinksScreen() {
  const [filter, setFilter] = React.useState(false);
  const [search, setSearch] = React.useState("");
  const [results, setResults] = React.useState([]);
  const [zipcode, setZipcode] = React.useState("");
  let itemObj = new Items();

  return (
    <View style={styles.container}>
      <SearchBar
        placeholder="Type Here..."
        value={search}
        onChangeText={(search) => {
          setSearch(search);
        }}
        onSubmitEditing={() => {
          // Geolocation.getCurrentPosition((info) => {
          //   axios
          //     .get(
          //       `https://maps.googleapis.com/maps/api/geocode/json?latlng=${info.coords.latitude},${info.coords.longitude}&key=AIzaSyDUAgs6Oz0iTMoHUzxuv95F4yN4ehY2xrc`
          //     )
          //     .then((result) => {
          //       let words = result.data.results[0].address_components;
          //       let postcode = words[words.length - 1].long_name;
          //       console.log(postcode);
          itemObj.loadAllMatch(search).then((search_result) => {
            setResults(search_result);
          });
          //     });
          // });
        }}
      />
      <ScrollView>
        <View
          style={{
            flexDirection: "row",
            justifyContent: "space-between",
            alignItems: "center",
            marginLeft: "15px",
            marginRight: "15px",
            marginTop: "15px"
          }}
        >
          <Text
            style={{
              fontFamily: "roboto-thin",
              fontSize: "30px"
            }}
          >
            Find items
          </Text>
          <Button
            type="outline"
            icon={<AntDesign name="filter" style={{ fontSize: "18px" }} />}
            buttonStyle={{
              borderColor: "black",
              padding: "4px"
            }}
            onPress={() => {
              setFilter(!filter);
            }}
          ></Button>
        </View>
        <View
          style={{
            flexDirection: "row",
            justifyContent: "flex-start",
            alignItems: "center",
            marginLeft: "15px",
            marginRight: "15px",
            marginTop: "15px"
          }}
        >
          <Text
            style={{
              fontFamily: "roboto-thin",
              fontSize: "14px"
            }}
          >
            Search for the items you want and add them to your list
          </Text>
        </View>

        {filter ? (
          <View
            style={{
              flexDirection: "row",
              justifyContent: "space-between",
              alignItems: "center",
              marginLeft: "15px",
              marginRight: "15px"
            }}
          >
            <Button title="Outline button" type="outline button" />
            <Button title="Outline button" type="outline button" />
            <Button title="Outline button" type="outline button" />
          </View>
        ) : null}
        <View
          style={{
            width: "100%",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            marginTop: "15px"
          }}
        >
          {results !== []
            ? results.map((resultObj) => {
                let i = 0;
                return (
                  <ItemCard
                    imageLink={resultObj.imageUrl}
                    key={resultObj.imageUrl}
                    itemObj={resultObj}
                    key={i++}
                  />
                );
              })
            : null}
        </View>
      </ScrollView>
    </View>
  );
}

function OptionButton({ icon, label, onPress, isLastOption }) {
  return (
    <RectButton
      style={[styles.option, isLastOption && styles.lastOption]}
      onPress={onPress}
    >
      <View style={{ flexDirection: "row" }}>
        <View style={styles.optionIconContainer}>
          <Ionicons name={icon} size={22} color="rgba(0,0,0,0.35)" />
        </View>
        <View style={styles.optionTextContainer}>
          <Text style={styles.optionText}>{label}</Text>
        </View>
      </View>
    </RectButton>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fafafa"
  },
  contentContainer: {
    paddingTop: 15
  },
  optionIconContainer: {
    marginRight: 12
  },
  option: {
    backgroundColor: "#fdfdfd",
    paddingHorizontal: 15,
    paddingVertical: 15,
    borderWidth: StyleSheet.hairlineWidth,
    borderBottomWidth: 0,
    borderColor: "#ededed"
  },
  lastOption: {
    borderBottomWidth: StyleSheet.hairlineWidth
  },
  optionText: {
    fontSize: 15,
    alignSelf: "flex-start",
    marginTop: 1
  }
});
