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

var a = [...Array(50).keys()];
var b = Array.from({ length: 50 }, () => Math.floor(Math.random() * 50));

const pdata = a.map(function (e, i) {
  return { index: e, value: b[i] };
});

const data = [
  { order_id: 1, seller: "A", buyer: "D", qunatity: 1, price: 10 },
  { order_id: 2, seller: "B", buyer: "E", qunatity: 2, price: 30 },
  { order_id: 3, seller: "C", buyer: "F", qunatity: 3, price: 20 },
];

function App() {
  return (
    <div className="Kodein">
      <ResponsiveContainer width="100%" aspect={3}>
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
  );
}
export default App;
