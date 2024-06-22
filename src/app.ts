import express, { Application } from 'express';
import morgan from 'morgan';
import routes from '../src/Product/Infrastructure/Routes/Routes';
import dotenv from 'dotenv';
import {Signale} from "signale";

const app: Application = express();
const signale = new Signale();

// Configurar middleware para analizar el cuerpo de las solicitudes JSON
app.use(express.json());

dotenv.config();
app.use(morgan('dev'));

const PORT = process.env.PORT || 3001;

const Segundo = process.env.SERVICE_NAME;

// Usa las rutas definidas en routes.ts
app.use('/', routes);

app.listen(PORT, () => {
  signale.success(`Servicio ${Segundo} corriendo en http://localhost:${PORT}`);
});
