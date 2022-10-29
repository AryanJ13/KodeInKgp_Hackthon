import React, { useState, useEffect } from "react";

const OrderBook = () => {
  const [orders, setOrders] = useState([]);
  const currencyPair = "btcusd";

  const currencyArray = currencyPair.toUpperCase().match(/.{1,3}/g);

  useEffect(() => {
    const subscribe = {
      event: "bts:subscribe",
      data: {
        channel: `order_book_${currencyPair}`,
      },
    };
    const ws = new WebSocket("wss://ws.bitstamp.net");

    ws.onopen = () => {
      ws.send(JSON.stringify(subscribe));
    };
    ws.onmessage = (event) => {
      const response = JSON.parse(event.data);
      setOrders(response.data);
    };
    ws.onclose = () => {
      ws.close();
    };

    return () => {
      ws.close();
    };
  }, [currencyPair]);

  const { bids, asks } = orders;
  const orderRows = (arr) =>
    arr &&
    arr
      .map((item, index) => (
        <tr key={index}>
          <td> {item[1]} </td>
          <td> {item[0]} </td>
        </tr>
      ))
      .slice(0, 10);
  const orderHead = (title) => (
    <thead>
      <tr>
        <th colSpan="2">{title}</th>
      </tr>
      <tr>
        <th>Amount ({currencyArray[0]})</th>
        <th>Price ({currencyArray[1]})</th>
      </tr>
    </thead>
  );
  return (
    <div>
      <h2 class="name">Crypto Order Book </h2>
      <div className="order-container">
        <table>
          {orderHead("Buy")}
          <tbody>{orderRows(bids)}</tbody>
        </table>

        <table>
          {orderHead("Sell")}
          <tbody>{orderRows(asks)}</tbody>
        </table>
      </div>
    </div>
  );
};

export default OrderBook;
