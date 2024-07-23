// MySQLConnection.ts

import { Sequelize, Model, DataTypes } from 'sequelize';
import { AProduct } from '../../Domain/Entities/AProduct';
import { Form } from '../../Domain/Entities/Form'; // Asegúrate de importar Form si no está importado


require('dotenv').config();

const sequelize = new Sequelize({
  dialect: 'mysql',
  host: process.env.DB_HOST_MYSQL,
  port: parseInt(process.env.DB_PORT_MYSQL || '3306', 10),
  database: process.env.DB_DATABASE_MYSQL,
  username: process.env.DB_USER_MYSQL,
  password: process.env.DB_PASSWORD_MYSQL,
});

class Product extends Model<AProduct> {}

Product.init({
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  product_uuid: { type: DataTypes.STRING, allowNull: false },
  name: { type: DataTypes.STRING, allowNull: false },
  precio: { type: DataTypes.FLOAT, allowNull: false },
  quantity: { type: DataTypes.INTEGER, allowNull: false },
  sales_description: { type: DataTypes.STRING, allowNull: false },
  category: { type: DataTypes.STRING, allowNull: false },
  uuid_Store:{type: DataTypes.STRING, allowNull: false},
  form: {type: DataTypes.JSON, allowNull: false },
  image: { type: DataTypes.STRING },
}, {
  sequelize,
  modelName: 'Product', // Nombre del modelo en singular
  tableName: 'products', // Nombre de la tabla en plural, según convención de Sequelize
  timestamps: false, // Si no necesitas timestamps de createdAt y updatedAt
});

// Sincronización de la base de datos (creación de tablas si no existen)
sequelize.sync().then(() => {
  console.log('Base de datos sincronizada correctamente.');
}).catch((error) => {
  console.error('Error al sincronizar la base de datos:', error);
});

export { sequelize, Product };
