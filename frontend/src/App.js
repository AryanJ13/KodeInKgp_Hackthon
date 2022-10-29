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

const data = [
  { order_id: 1, seller: "A", buyer: "D", qunatity: 1, price: 10 },
  { order_id: 2, seller: "B", buyer: "E", qunatity: 2, price: 30 },
  { order_id: 3, seller: "C", buyer: "F", qunatity: 3, price: 20 },
  { order_id: 4, seller: "Q", buyer: "E", qunatity: 4, price: 40 },
  { order_id: 5, seller: "W", buyer: "R", qunatity: 2, price: 50 },
];

const user_data = [
    {user_id: 1, balance: '$50', qunatity: 2},
    {user_id: 2, balance: '$60', qunatity: 3},
    {user_id: 3, balance: '$80', qunatity: 2},
]

function App() {
  const [b, setB] = useState([...Array(50).keys()]);

  fetch("/price").then((res) =>
    res.json().then((data) => {
      setB(data.slice(0, 100).reverse());
    })
  );

  var pdata = times.map(function (e, i) {
    return { index: e, value: b[i + 18] };
  });

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
            dataKey="value"
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
          {user_data.map((val, key) => {
            return (
              <tr key={key}>
                <td>{val.user_id}</td>
                <td>{val.balance}</td>
                <td>{val.qunatity}</td>
              </tr>
            );
          })}
        </table>
      </div>


    </div>
  );
}
export default App;
