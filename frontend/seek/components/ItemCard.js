import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import clsx from "clsx";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import Collapse from "@material-ui/core/Collapse";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import { red } from "@material-ui/core/colors";
import FavoriteIcon from "@material-ui/icons/Favorite";
import ShareIcon from "@material-ui/icons/Share";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import { View, Text } from "react-native";
import { Entypo, AntDesign } from "@expo/vector-icons";
import { ListItem } from "react-native-elements";
import { Items } from "../back_utils/Items.js";

const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: 345
  },
  media: {
    height: 0,
    paddingTop: "56.25%" // 16:9
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest
    })
  },
  expandOpen: {
    transform: "rotate(180deg)"
  },
  avatar: {
    backgroundColor: red[500]
  }
}));

export default function RecipeReviewCard(props) {
  const classes = useStyles();
  const [expanded, setExpanded] = React.useState(false);
  const itemObj = new Items();
  const itemInfo = [];
  let addresses = props.itemObj.address;
  let availabilities = props.itemObj.availability;
  let distances = props.itemObj.distance;
  let prices = props.itemObj.price;
  for (let i = 0; i < addresses.length; i++) {
    itemInfo.push({
      address: addresses[i],
      availability: availabilities[i],
      distance: distances[i],
      price: prices[i]
    });
  }

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Card
      className={classes.root}
      style={{ marginBottom: "10px", width: "90%" }}
    >
      <CardContent>
        <CardMedia
          className={classes.media}
          image={`${props.imageLink}`}
          title="Paella dish"
        />
        <Typography variant="body2" color="textSecondary" component="p">
          {props.itemObj.product_name}
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        <IconButton
          aria-label="add to favorites"
          onClick={() => {
            itemObj.addItemToCart(props.itemObj);
          }}
        >
          <FavoriteIcon />
        </IconButton>
        <IconButton aria-label="share">
          <ShareIcon />
        </IconButton>
        <IconButton
          className={clsx(classes.expand, {
            [classes.expandOpen]: expanded
          })}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </IconButton>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          <Typography paragraph>Available places:</Typography>
          <View
            style={{
              width: "100%"
            }}
          >
            {itemInfo.map((singleItemInfo) => {
              let i = 0;
              return (
                <ListItem
                  key={i++}
                  leftAvatar={
                    singleItemInfo.availability ? (
                      <AntDesign
                        name="checkcircleo"
                        style={{ marginRight: "5px" }}
                      />
                    ) : (
                      <Entypo
                        name="cross"
                        style={{ marginRight: "5px" }}
                      ></Entypo>
                    )
                  }
                  containerStyle={{
                    padding: "5px"
                  }}
                  title={singleItemInfo.address}
                  subtitle={`distance: ${singleItemInfo.distance}mi  price: $${singleItemInfo.price}`}
                  bottomDivider
                />
              );
            })}
          </View>
        </CardContent>
      </Collapse>
    </Card>
  );
}
