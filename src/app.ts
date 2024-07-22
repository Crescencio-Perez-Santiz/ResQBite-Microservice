
import express, { Application, Request, Response, NextFunction } from "express";
import morgan from "morgan";
import dotenv from 'dotenv';
import { Signale } from "signale";
import proxy from "express-http-proxy";
import https from 'https';
import fs from 'fs';
import path from 'path';
import { validateToken } from './middleware/authMiddleware';
import jwt, { JwtPayload } from 'jsonwebtoken';

const app: Application = express();
const signale = new Signale();

dotenv.config();
app.use(morgan('dev'));
const PORT = process.env.PORT || 3000;
const GATEWAY = process.env.SERVICE_NAME;

declare global {
    namespace Express {
        interface Request {
            user?: string | JwtPayload;
        }
    }
}

// Aplicar validación de token
app.use(validateToken);

app.use('/api/v1/user', proxy('https://resqbite-user.integrador.xyz:5000'));//USER
app.use('/api/v4/store', proxy('https://resqbite-store.integrador.xyz:5001'));//STORE
app.use('/api/v3/order', proxy('http://127.0.0.1:5003'));//ORDER
app.use('/api/v2/payment', proxy('https://resqbite-payment.integrador.xyz:4242')); // PAYMENT
app.use('/api/v5/product', proxy('http://50.19.235.254:3001')); // PRODUCT

// Certificado
const httpsOptions = {
    key: fs.readFileSync(path.join(__dirname, 'privkey.pem')),
    cert: fs.readFileSync(path.join(__dirname, 'fullchain.pem'))
};

// servidor HTTPS
https.createServer(httpsOptions, app).listen(PORT, () => {
    signale.success(`Servicio ${GATEWAY} corriendo en https://localhost:${PORT}`);
});
