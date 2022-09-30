import axios from "axios";
import React from "react";

import Box from "@mui/material/Box";

import Chart from "./Chart";
import Total from "./Total";
import ExchangeTable from "./ExchangeTable";
import Item from "./Item";

const baseURL = "http://localhost:8000/";

export default function Exchange() {
  const [data, setData] = React.useState(null);

  React.useEffect(() => {
    const intervalCall = setInterval(() => {
      axios.get(baseURL).then((response) => {
        setData(response.data);
      });
    }, 4000);
    return () => {
      clearInterval(intervalCall);
    };
  }, []);
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
