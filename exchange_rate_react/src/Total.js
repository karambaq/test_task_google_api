import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";

export default function Total(props) {
  return (
    <Card raised>
      <CardContent>
        <Typography variant="h5" component="div">
          Total USD $
        </Typography>
        <Typography sx={{ fontSize: 25 }} color="green" gutterBottom>
          {props.data.reduce((accumulator, object) => {
            return accumulator + object.price_usd;
          }, 0)}
        </Typography>
      </CardContent>
    </Card>
  );
}
