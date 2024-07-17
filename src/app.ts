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

app.use('/api/v1/user',proxy('http://127.0.0.1:3001'));
app.use('/api/v2/payment', proxy('http://127.0.0.1:3002'));
app.use('/api/v3/order',proxy('http://127.0.0.1:3003'));
app.use('/api/v4/store', proxy('http://127.0.0.1:3004'));
app.use('/api/v5/product',proxy('http://127.0.0.1:3005'));


app.listen(PORT, () => {
    signale.success(`Servicio ${GATEWAY} corriendo en http://localhost:${PORT}`);
});