// MySQLProductRepository.ts

import { AProduct } from '../../Domain/Entities/AProduct';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { Product } from '../Config/mysqlConnection';

export class MySQLProductRepository implements IProductRepository {

  async save(product: AProduct): Promise<AProduct> {
    try {
      const savedProduct = await Product.create({
        product_uuid: product.product_uuid,
        name: product.name,
        precio: product.precio,
        quantity: product.quantity,
        sales_description: product.sales_description,
        category: product.category,
        uuid_Store: product.uuid_Store,
        image: product.image,
        form: {
          description: product.form.description,
          creation_date: product.form.creation_date,
          approximate_expiration_date: product.form.approximate_expiration_date,
          quality: product.form.quality,
          manipulation: product.form.manipulation
        }
      });

      return savedProduct.toJSON() as AProduct;
    } catch (error) {
      throw new Error(`Failed to save product: ${error}`);
    }
  }

  async listAll(): Promise<AProduct[]> {
    try {
      const products = await Product.findAll();
      return products.map(p => p.toJSON() as AProduct);
    } catch (error) {
      throw new Error(`Failed to list products: ${error}`);
    }
  }

  async get_by_uuid(product_uuid: string): Promise<AProduct | null> {
    try {
      const product = await Product.findOne({ where: { product_uuid } });
      return product ? product.toJSON() as AProduct : null;
    } catch (error) {
      throw new Error(`Failed to find product by UUID: ${error}`);
    }
  }

  async get_by_id(id: string): Promise<AProduct | null> {
    try {
      const product = await Product.findByPk(id);
      return product ? product.toJSON() as AProduct : null;
    } catch (error) {
      throw new Error(`Failed to find product by ID: ${error}`);
    }
  }

  async delete(product_uuid: string): Promise<void> {
    try {
      await Product.destroy({ where: { product_uuid } });
    } catch (error) {
      throw new Error(`Failed to delete product: ${error}`);
    }
  }

  async update(id: string, productData: Partial<AProduct>): Promise<AProduct> {
    try {
      // Intentar actualizar el producto con los datos proporcionados
      const [affectedRows] = await Product.update(productData, {
        where: { id },
        returning: true,
      });
  
      // Verificar si alguna fila fue afectada por la actualización
      if (affectedRows === 0) {
        throw new Error('Product not found');
      }
  
      // Obtener el producto actualizado
      const updatedProduct = await Product.findByPk(id);
      if (!updatedProduct) {
        throw new Error('Product not found');
      }
  
      return updatedProduct.toJSON() as AProduct;
    } catch (error) {
      throw new Error(`Failed to update product: ${error}`);
    }
  }

  async getByUuidStore(uuid_Store: string): Promise<AProduct[]> {
    try {
      const products = await Product.findAll({ where: { uuid_Store } });
      return products.map(product => product.toJSON() as AProduct);
    } catch (error) {
      if (error instanceof Error) {
        throw new Error(`Failed to find products by store UUID: ${error.message}`);
      }
      throw error;
    }
  }
  
 
}
