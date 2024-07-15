import { v4 as uuidv4 } from 'uuid';
import { Form } from './Form';


export class AProduct {
  product_uuid: string;
  name: string;
  precio: number;
  quantity: number;
  sales_description: string;
  category: string;
  form: Form;
  image?: string; // Hacer el campo de imagen opcional

  constructor(name: string, precio: number, quantity: number, sales_description: string, category: string, form: Form, image?: string) {
    this.product_uuid = uuidv4();
    this.name = name;
    this.precio = precio;
    this.quantity = quantity;
    this.sales_description = sales_description;
    this.category = category;
    this.image = image; // Inicializar el campo de imagen si se proporciona
    this.form = form;
  }
}
