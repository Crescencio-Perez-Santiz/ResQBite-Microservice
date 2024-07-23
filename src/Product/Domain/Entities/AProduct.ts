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
  uuid_Store:string;
  image?: string; 

  constructor(name: string, precio: number, quantity: number, sales_description: string, category: string ,form:Form,  uuid_Store:string, image?: string) {
    this.product_uuid = uuidv4();
    this.name = name;
    this.precio = precio;
    this.quantity = quantity;
    this.sales_description = sales_description;
    this.category = category;
    this.form=form;
    this.uuid_Store = uuid_Store;
    this.image = image; 
    
    
  }
}
