import React from "react";
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

var a = [...Array(50).keys()];
var b = Array.from({ length: 50 }, () => Math.floor(Math.random() * 50));
b.sort();

const pdata = a.map(function (e, i) {
  return { index: e, value: b[i] };
});

const data = [
  { order_id: 1, seller: "A", buyer: "D", qunatity: 1, price: 10 },
  { order_id: 2, seller: "B", buyer: "E", qunatity: 2, price: 30 },
  { order_id: 3, seller: "C", buyer: "F", qunatity: 3, price: 20 },
  { order_id: 4, seller: "Q", buyer: "E", qunatity: 4, price: 40 },
  { order_id: 5, seller: "W", buyer: "R", qunatity: 2, price: 50 },
];

function App() {
  return (
    <div className="Kodein">
        <div class ="heading">
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
    </div>
  );
}
export default App;
