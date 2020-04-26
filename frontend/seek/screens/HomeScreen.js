import * as React from "react";
import { Platform, StyleSheet, View, Text, ScrollView } from "react-native";
import { Button, SearchBar } from "react-native-elements";
import { Ionicons, AntDesign, EvilIcons } from "@expo/vector-icons";
import ItemCard from "../components/ItemCard.js";
import { Items } from "../back_utils/Items.js";

export default function HomeScreen() {
  const [filter, setFilter] = React.useState(false);
  const [search, setSearch] = React.useState("");
  const [cart, setCart] = React.useState([]);
  let itemObj = new Items();

  itemObj.getAllItemsFromCart().then((cartItems) => {
    console.log(cartItems);
    setCart(cartItems);
  });
  return (
    <View style={styles.container}>
      <SearchBar
        placeholder="Type Here..."
        value={search}
        onChangeText={(search) => {
          setSearch(search);
        }}
        onSubmitEditing={() => {
          console.log(search);
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
            Your cart
          </Text>
          <Button
            type="outline"
            icon={<EvilIcons name="refresh" style={{ fontSize: "18px" }} />}
            buttonStyle={{
              borderColor: "black",
              padding: "4px"
            }}
            onPress={() => {
              itemObj.getAllItemsFromCart().then((cartItems) => {
                console.log(cartItems);
                setCart(cartItems);
              });
            }}
          ></Button>
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
          {cart.map((cartItem) => {
            let i = 0;
            return (
              <ItemCard
                imageLink={cartItem.imageUrl}
                key={cartItem.imageUrl}
                itemObj={cartItem}
                key={i++}
              />
            );
          })}
        </View>
      </ScrollView>
    </View>
  );
}

HomeScreen.navigationOptions = {
  header: null
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "rgb(250,250,250)"
  },
  developmentModeText: {
    marginBottom: 20,
    color: "rgba(0,0,0,0.4)",
    fontSize: 14,
    lineHeight: 19,
    fontFamily: "Montserrat",
    textAlign: "center"
  },
  contentContainer: {
    paddingTop: 30
  },
  welcomeContainer: {
    alignItems: "center",
    marginTop: 10,
    marginBottom: 20
  },
  welcomeImage: {
    width: 100,
    height: 80,
    resizeMode: "contain",
    marginTop: 3,
    marginLeft: -10
  },
  getStartedContainer: {
    alignItems: "center",
    marginHorizontal: 50
  },
  homeScreenFilename: {
    marginVertical: 7
  },
  codeHighlightText: {
    color: "rgba(96,100,109, 0.8)"
  },
  codeHighlightContainer: {
    backgroundColor: "rgba(0,0,0,0.05)",
    borderRadius: 3,
    paddingHorizontal: 4
  },
  getStartedText: {
    fontSize: 17,
    color: "rgba(96,100,109, 1)",
    lineHeight: 24,
    textAlign: "center"
  },
  tabBarInfoContainer: {
    position: "absolute",
    bottom: 0,
    left: 0,
    right: 0,
    ...Platform.select({
      ios: {
        shadowColor: "black",
        shadowOffset: { width: 0, height: -3 },
        shadowOpacity: 0.1,
        shadowRadius: 3
      },
      android: {
        elevation: 20
      }
    }),
    alignItems: "center",
    backgroundColor: "#fbfbfb",
    paddingVertical: 20
  },
  tabBarInfoText: {
    fontSize: 17,
    color: "rgba(96,100,109, 1)",
    textAlign: "center"
  },
  navigationFilename: {
    marginTop: 5
  },
  helpContainer: {
    marginTop: 15,
    alignItems: "center"
  },
  helpLink: {
    paddingVertical: 15
  },
  helpLinkText: {
    fontSize: 14,
    color: "#2e78b7"
  }
});
