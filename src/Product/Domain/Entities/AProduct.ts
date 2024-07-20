import { v4 as uuidv4 } from 'uuid';
import { Form } from './Form';


export class AProduct {
  id?: number;
  product_uuid: string;
  name: string;
  precio: number;
  quantity: number;
  sales_description: string;
  category: string;
  form:Form;
  id_Store:number;
  image?: string; 

  constructor(name: string, precio: number, quantity: number, sales_description: string, category: string ,form:Form,  id_Store:number, image?: string) {
    this.product_uuid = uuidv4();
    this.name = name;
    this.precio = precio;
    this.quantity = quantity;
    this.sales_description = sales_description;
    this.category = category;
    this.form=form;
    this.id_Store = id_Store;
    this.image = image; 
    
    
  }
}
