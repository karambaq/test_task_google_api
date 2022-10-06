import React from "react";

import Box from "@mui/material/Box";

import Chart from "./Chart";
import Total from "./Total";
import ExchangeTable from "./ExchangeTable";
import Item from "./Item";


var ws = new WebSocket("ws://localhost/ws/orders/");

export default function Exchange() {
  let [data, setData] = React.useState(null);

    React.useEffect(() => {

        let allData;
        ws.onopen = function (e) {
            ws.send(
                JSON.stringify({
                    action: "list",
                    request_id: new Date().getTime(),
                })
            );
        };

        ws.onmessage = function (e) {
            allData = JSON.parse(e.data);
            console.log(allData);
            setData(allData)
        }
    })
  if (!data) return null;

  return (
    <Box
      m={2}
      pt={3}
      sx={{
        display: "grid",
        gridAutoFlow: "row",
        gridTemplateColumns: "repeat(2, 1fr)",
        gridTemplateRows: "repeat(2, 50px)",
        gap: 1,
      }}
    >
      <Item sx={{ gridColumn: "1", gridRow: "1 / 3" }}>
        <ExchangeTable data={data}></ExchangeTable>
      </Item>
      <Item sx={{ gridColumn: "2", gridRow: "1 / 4" }}>
        <Total data={data}></Total>
      </Item>
      <Item sx={{ gridColumn: "2" }}>
        <Chart data={data}></Chart>
      </Item>
    </Box>
  );
}
