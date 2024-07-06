import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';

export class GetProductByIdUseCase {
  constructor(private repository: IProductRepository) {}

  async execute(productId: string): Promise<AProduct | { error: string }> {
    try {
      const product = await this.repository.get_by_id(productId);
      if (!product) {
        return { error: 'Product not found' };
      }
      return product;
    } catch (error: any) {
      return { error: error.toString() };
    }
  }
}
