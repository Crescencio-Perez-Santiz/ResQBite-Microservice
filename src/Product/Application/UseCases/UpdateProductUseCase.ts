import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';

export class UpdateProductUseCase {
  constructor(private repository: IProductRepository) {}

  async execute(productId: string, productData: Partial<AProduct>): Promise<AProduct | { error: string }> {
    try {
      const updatedProduct = await this.repository.update(productId, productData);
      return updatedProduct;
    } catch (error: any) {
      return { error: error.toString() };
    }
  }
}
