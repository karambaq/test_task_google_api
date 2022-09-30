import {
  LineChart,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Line,
} from "recharts";

import Card from "@mui/material/Card";

export default function Chart(props) {
  return (
    <Card raised>
      <LineChart
        width={700}
        height={400}
        data={props.data}
        margin={{ top: 0, right: 20, left: 10, bottom: 5 }}
      >
        <XAxis dataKey="delivery_date" />
        <YAxis dataKey="price_rub" />
        <Tooltip />
        <CartesianGrid stroke="#f5f5f5" />
        <Line
          type="monotone"
          dataKey="price_rub"
          stroke="#387908"
          yAxisId={0}
        />
      </LineChart>
    </Card>
  );
}
