import { createConnection, Entity, PrimaryGeneratedColumn, Column } from 'typeorm';
import { config } from 'dotenv';

config();

console.log('DB_HOST_MYSQL:', process.env.DB_HOST_MYSQL);
console.log('DB_USER_MYSQL:', process.env.DB_USER_MYSQL);
console.log('DB_PASSWORD_MYSQL:', process.env.DB_PASSWORD_MYSQL);
console.log('DB_DATABASE_MYSQL:', process.env.DB_DATABASE_MYSQL);

@Entity('products')
export class ProductModel {
  @PrimaryGeneratedColumn()
  id!: number;

  @Column({ length: 36, unique: true })
  product_uuid!: string;

  @Column({ length: 50, unique: true })
  name!: string;

  @Column('float')
  precio!: number;

  @Column('int')
  stock!: number;

  toDict(): Record<string, any> {
    return {
      id: this.id,
      product_uuid: this.product_uuid,
      name: this.name,
      precio: this.precio,
      stock: this.stock,
    };
  }
}

export class DBConnection {
  constructor() {
    try {
      createConnection({
        type: 'mysql',
        host: process.env.DB_HOST_MYSQL,
        port: parseInt(process.env.DB_PORT_MYSQL!),
        username: process.env.DB_USER_MYSQL!,
        password: process.env.DB_PASSWORD_MYSQL!,
        database: process.env.DB_DATABASE_MYSQL!,
        entities: [ProductModel],
        synchronize: true,
       
      }).then(() => {
        console.log('Conexión exitosa a la base de datos con MySQL LISTA!');
      });
    } catch (e) {
      console.error(`Error al conectar a la base de datos: ${e}`);
    }
  }
}

const dbConnection = new DBConnection();
