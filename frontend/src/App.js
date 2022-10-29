import React, { useState } from "react";
import {
  AreaChart,
  ResponsiveContainer,
  Legend,
  Tooltip,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";
import "./App.css";
import OrderBook from "./OrderBook";

var times = [...Array(50).keys()];
for (let i = 0; i < times.length; i++) {
  var timestamp = Date.now() - i * 600;
  var date = new Date(timestamp);
  times[i] = String(date.getMinutes()).padStart(2, '0') + ":" + String(date.getSeconds()).padStart(2, '0')
}
times.reverse()

// true == Market, false == limit
var order_type = true

// const data = [
//   { order_id: 1, seller: "A", buyer: "D", qunatity: 1, price: 10 },
//   { order_id: 2, seller: "B", buyer: "E", qunatity: 2, price: 30 },
//   { order_id: 3, seller: "C", buyer: "F", qunatity: 3, price: 20 },
//   { order_id: 4, seller: "Q", buyer: "E", qunatity: 4, price: 40 },
//   { order_id: 5, seller: "W", buyer: "R", qunatity: 2, price: 50 },
// ];

function update_prices(b, setB) {

  fetch("/price").then((res) =>
    res.json().then((data) => {
      setB(data.slice(0, 100).reverse());
    })
  );

  return times.map(function (e, i) {
    return { index: e, Price: b[i + 18] };
  });
}

function update_tradebook(data, setData) {
  fetch("/tradebook").then((res) =>
    res.json().then((data) => {
      setData(data.slice(0, 10));
    })
  );
}

function update_user(user, setUser) {
  fetch("/user").then((res) =>
    res.json().then((data) => {
      setUser(data.slice(0, 5));
    })
  );
}

function App() {
  const [b, setB] = useState([]);
  const [data, setData] = useState([]);
  const [user, setUser] = useState([]);
  const [userid, setUserId] = useState("");
  const [stockAmount, setStockAmount] = useState("");
  const [price, setPrice] = useState("");
  const buyClick = () => {
    var url = "/order?" + "user_id=" + userid + "&qty=" + stockAmount + "&price=" + price + "&bos=1&mol=" + (order_type ? "1" : "0");
    fetch(url, { method: "POST" })
  };
  const sellClick = () => {
    var url = "/order?" + "user_id=" + userid + "&qty=" + stockAmount + "&price=" + price + "&bos=0&mol=" + (order_type ? "1" : "0");
    fetch(url, { method: "POST" })
  };

  var pdata = update_prices(b, setB);
  var market_price = b[67];
  update_tradebook(data, setData);
  update_user(user, setUser);
  return (
    <div className="Kodein">
      <div class="heading">
        <h1>Stock Market Auction</h1>
      </div>
      <ResponsiveContainer width="75%" aspect={2.8}>
        <AreaChart data={pdata} margin={{ right: 300 }}>
          <defs>
            <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8} />
              <stop offset="95%" stopColor="#8884d8" stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="index" interval={"preserveStartEnd"} />
          <YAxis></YAxis>
          <Legend />
          <Tooltip />
          <Area
            dataKey="Price"
            stroke="#8884d8"
            fillOpacity={1}
            fill="url(#colorUv)"
          />
        </AreaChart>
      </ResponsiveContainer>
      <div class="tradebook">
        <table>
          <tr>
            <th>Order Id</th>
            <th>Seller</th>
            <th>Buyer</th>
            <th>Quantity</th>
            <th>Price</th>
          </tr>
          {data.map((val, key) => {
            return (
              <tr key={key}>
                <td>{val.order_id}</td>
                <td>{val.seller}</td>
                <td>{val.buyer}</td>
                <td>{val.qunatity}</td>
                <td>{val.price}</td>
              </tr>
            );
          })}
        </table>
      </div>
      <div>
        <OrderBook />
      </div>

      <div class="usertable">
        <table>
          <tr>
            <th>User ID</th>
            <th>Balance</th>
            <th>Quantity</th>
          </tr>
          {user.map((val, key) => {
            return (
              <tr key={key}>
                <td>{val.user_id}</td>
                <td>{val.balance}</td>
                <td>{val.quantity}</td>
              </tr>
            );
          })}
        </table>
      </div>
      <div class="market">
        <h4>Current Market price: {market_price}</h4>
      </div>
      <div class="actions">
        <button className="buttonB" type="button" onClick={buyClick} size="lg">Buy</button>
        <button className="buttonB" type="button" onClick={sellClick} size="lg">Sell</button>
      </div>
      <div>
        <Button> </Button>
      </div>
      <div class="data">
        <form>
          <label>User ID
            <input
              type="text"
              value={userid}
              onChange={(e) => setUserId(e.target.value)}
            />
          </label>
        </form>
        <form class="amount">
          <label>Stock Amount
            <input
              type="text"
              value={stockAmount}
              onChange={(e) => setStockAmount(e.target.value)}
            />
          </label>
        </form>
        <form class="price">
          <label>Price
            <input
              type="text"
              value={price}
              onChange={(e) => setPrice(e.target.value)}
            />
          </label>
        </form>
      </div>
    </div>
  );
}

class Button extends React.Component {
  state = {
    textflag: false,
  }

  ToggleButton() {
    this.setState(
      { textflag: !this.state.textflag }
    );
    order_type = !this.state.textflag
  }

  render() {
    return (
      <div>
        <button class="orderB" onClick={() => this.ToggleButton()} size="lg">
          {this.state.textflag === false ? "Market" : "Limit"}
        </button>
        {!this.state.textflag && this.props.text}
      </div>
    )
  }
}

export default App;
