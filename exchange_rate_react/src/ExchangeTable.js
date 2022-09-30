import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Card from "@mui/material/Card";

export default function ExchangeTable(props) {
  return (
    <Card raised>
      <TableContainer component={Paper}>
        <Table size="small" aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Номер</TableCell>
              <TableCell>Номер заказа</TableCell>
              <TableCell>Стоимость в $</TableCell>
              <TableCell>Стоимость в ₽</TableCell>
              <TableCell>Срок доставки</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {props.data.map((obj) => (
              <TableRow
                key={obj.id}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell> {obj.id} </TableCell>
                <TableCell> {obj.order_id} </TableCell>
                <TableCell> {obj.price_usd} </TableCell>
                <TableCell> {obj.price_rub} </TableCell>
                <TableCell> {obj.delivery_date} </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Card>
  );
}
