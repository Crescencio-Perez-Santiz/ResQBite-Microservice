import { v4 as uuidv4 } from 'uuid';

export class AProduct {
  product_uuid: string;
  name: string;
  precio: number;
  stock: number;

  constructor(name: string, precio: number, stock: number) {
    // Generar un UUID único para el producto
    this.product_uuid = uuidv4();
    this.name = name;
    this.precio = precio;
    this.stock = stock;
  }

  toDict(): Record<string, any> {
    return {
      product_uuid: this.product_uuid,
      name: this.name,
      precio: this.precio,
      stock: this.stock,
    };
  }
}
