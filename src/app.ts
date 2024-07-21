import express, {Application, Request, Response} from "express";
import morgan from "morgan";
import dotenv from 'dotenv';
import {Signale} from "signale";
import proxy from "express-http-proxy";

const app:Application = express();
const signale = new Signale();

dotenv.config();
app.use(morgan('dev'));
const PORT = process.env.PORT || 3000;
const GATEWAY = process.env.SERVICE_NAME;

app.use('/api/v1/user',proxy('http://3.221.197.10:5000'));
app.use('/api/v4/store', proxy('http://52.1.97.242:5001'));
app.use('/api/v3/order',proxy('http://127.0.0.1:5003'));

app.use('/api/v2/payment', proxy('http://3.227.128.249:4242'));
app.use('/api/v5/',proxy('http://50.19.235.254:3001'));


app.listen(PORT, () => {
    signale.success(`Servicio ${GATEWAY} corriendo en http://localhost:${PORT}`);
});
