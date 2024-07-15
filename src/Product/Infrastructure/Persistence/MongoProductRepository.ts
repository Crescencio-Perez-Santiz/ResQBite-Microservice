import { model, Schema } from 'mongoose';
import { AProduct } from '../../Domain/Entities/AProduct';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';

const ProductSchema = new Schema<AProduct>({
  
  product_uuid: { type: String, required: true, unique: true },
  name: { type: String, required: true },
  precio: { type: Number, required: true },
  quantity: { type: Number, required: true },
  sales_description: { type: String, required: true },
  category: { type: String, required: true },
  image: { type: String }, // Añadir el campo de imagen como opcional
  form: {
    description: { type: String, required: true },
    creation_date: { type: String, required: true },
    approximate_expiration_date: { type: String, required: true },
    quality: { type: String, required: true },
    manipulation: { type: String, required: true }
  }
}, {
  versionKey: false // Elimina `__v`
});


const ProductModel = model<AProduct>('Product', ProductSchema);

export class MongoProductRepository implements IProductRepository {
  async save(product: AProduct): Promise<AProduct> {
    try {
      const productDocument = new ProductModel(product);
      await productDocument.save();
      return productDocument.toObject();
    } catch (error) {
      throw new Error(`Failed to save product: ${error}`);
    }
  }

  async listAll(): Promise<AProduct[]> {
    return await ProductModel.find().exec();
  }

  async get_by_uuid(id: string): Promise<AProduct | null> {
    return ProductModel.findOne({ product_uuid: id }).exec();
  }

  async get_by_id(id: string): Promise<AProduct | null> {
    return ProductModel.findById(id).exec();
  }
  
  async delete(id: string): Promise<void> {
    await ProductModel.findByIdAndDelete(id).exec();
  }

  async update(id: string, productData: Partial<AProduct>): Promise<AProduct> {
    const updatedProduct = await ProductModel.findByIdAndUpdate(id, productData, { new: true }).exec();
    if (!updatedProduct) {
      throw new Error('Product not found');
    }
    return updatedProduct.toObject();
  }
}
