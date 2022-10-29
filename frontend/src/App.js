import React from "react";
import "./App.css";

const data = [
    {order_id: 1, seller: "A", buyer: "D", qunatity: 1, price: 10},
    {order_id: 2, seller: "B", buyer: "E", qunatity: 2, price: 30},
    {order_id: 3, seller: "C", buyer: "F", qunatity: 3, price: 20},
  ]
    
  function App() {
    return (
      <div className="App">
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
            )
          })}
        </table>
      </div>
    );
  }
export default App;