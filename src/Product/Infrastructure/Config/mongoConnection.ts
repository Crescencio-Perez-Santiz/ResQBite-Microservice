import mongoose from 'mongoose';
import { config } from 'dotenv';

config();

const mongoUri = `mongodb://${process.env.DB_HOST_MONGODB}:${process.env.DB_PORT_MONGODB}/${process.env.DB_DATABASE_MONGODB}`;

export const mongoConnection = async () => {
  try {
    await mongoose.connect(mongoUri, {
      user: process.env.DB_USER_MONGODB,
      pass: process.env.DB_PASSWORD_MONGODB,
      authSource: 'admin', // Agrega authSource si es necesario
    });
    console.log('Conexión exitosa a la base de datos con MongoDB LISTA!');
  } catch (error) {
    console.error('Error al conectar a la base de datos de MongoDB:', error);
  }
};
