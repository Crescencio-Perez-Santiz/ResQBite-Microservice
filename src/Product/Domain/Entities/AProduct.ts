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

  constructor(name: string, precio: number, quantity: number, sales_description: string, category: string, form:Form) {
    this.product_uuid = uuidv4();
    this.name = name;
    this.precio = precio;
    this.quantity = quantity;
    this.sales_description = sales_description;
    this.category = category;
    this.form= form
  }


}
