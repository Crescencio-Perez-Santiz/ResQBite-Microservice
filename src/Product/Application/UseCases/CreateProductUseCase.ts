import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';


export class CreateProductUseCase {
  constructor(private repository: IProductRepository) {}

  async execute(productData: AProduct): Promise<AProduct | { error: string }> {
    try {
      const product = await this.repository.save(productData);
      return product;
    } catch (error:any) {
      return { error: error.toString() };
    }
  }
}
