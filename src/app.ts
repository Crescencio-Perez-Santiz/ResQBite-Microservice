import express, { Application } from 'express';
import morgan from 'morgan';
import routes from './Product/Interfaces/Delivery/Routes';
import dotenv from 'dotenv';
import { mongoConnection } from './Product/Infrastructure/Config/mongoConnection';

const app: Application = express();
dotenv.config();
app.use(morgan('dev'));

const PORT = process.env.PORT || 3001;
const SERVICE_NAME = process.env.SERVICE_NAME || 'Unknown Service';

mongoConnection();

// Middleware para analizar el cuerpo de las solicitudes JSON
app.use(express.json());

app.use('/', routes);
app.listen(PORT, () => {
  console.log(`Servicio ${SERVICE_NAME} corriendo en http://localhost:${PORT}`);
});
