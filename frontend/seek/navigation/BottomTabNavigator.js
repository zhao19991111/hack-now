import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import * as React from "react";

import TabBarIcon from "../components/TabBarIcon";
import HomeScreen from "../screens/HomeScreen";
import LinksScreen from "../screens/LinksScreen";

import Colors from "../constants/Colors.js";

const BottomTab = createBottomTabNavigator();
const INITIAL_ROUTE_NAME = "Cart";

export default function BottomTabNavigator({ navigation, route }) {
  // Set the header title on the parent stack navigator depending on the
  // currently active tab. Learn more in the documentation:
  // https://reactnavigation.org/docs/en/screen-options-resolution.html
  // navigation.setOptions({ headerTitle: getHeaderTitle(route) });

  return (
    <BottomTab.Navigator
      initialRouteName={INITIAL_ROUTE_NAME}
      tabBarOptions={{
        activeTintColor: Colors.tabIconSelected,
        labelStyle: {
          fontFamily: "roboto-regular"
        }
      }}
    >
      <BottomTab.Screen
        name="Cart"
        component={HomeScreen}
        options={{
          title: "Cart",
          tabBarIcon: ({ focused }) => (
            <TabBarIcon focused={focused} name="ios-heart" />
          )
        }}
      />
      <BottomTab.Screen
        name="Links"
        component={LinksScreen}
        options={{
          title: "Find items",
          tabBarIcon: ({ focused }) => (
            <TabBarIcon focused={focused} name="ios-cart" />
          )
        }}
      />
    </BottomTab.Navigator>
  );
}

function getHeaderTitle(route) {
  const routeName =
    route.state?.routes[route.state.index]?.name ?? INITIAL_ROUTE_NAME;

  switch (routeName) {
    case "Cart":
      return "How to get started";
    case "Links":
      return "Links to learn more";
  }
}
