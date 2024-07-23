import express, { Application } from 'express';
import morgan from 'morgan';
import routes from './Product/Interfaces/Delivery/Routes';
import dotenv from 'dotenv';
import { sequelize } from './Product/Infrastructure/Config/mysqlConnection';
import { connect as connectRabbitMQ } from './Product/Infrastructure/Config/rabbitMQConfig';
import https from 'https';
import fs from 'fs';
import path from 'path';

const app: Application = express();
dotenv.config();
app.use(morgan('dev'));

const PORT = process.env.PORT || 3001;
const SERVICE_NAME = process.env.SERVICE_NAME || 'Unknown Service';

app.use(express.json());

sequelize
  .sync()
  .then(() => {
    console.log('Database connected');
  })
  .catch((error: Error) => {
    console.error('Unable to connect to the database:', error);
  });

connectRabbitMQ()
  .then(() => {
    console.log('RabbitMQ connected');
  })
  .catch((error: Error) => {
    console.error('Unable to connect to RabbitMQ:', error);
  });

app.use('/', routes);

// Leer los certificados SSL
const httpsOptions = {
  key: fs.readFileSync(path.join(__dirname, 'privkey.pem')),
  cert: fs.readFileSync(path.join(__dirname, 'fullchain.pem'))
};

// Crear el servidor HTTPS
https.createServer(httpsOptions, app).listen(PORT, () => {
  console.log(`Servicio ${SERVICE_NAME} corriendo en https://localhost:${PORT}`);
});

export default app;
