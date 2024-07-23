import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';

export class GetProductByUuidStoreUseCase {
  constructor(private productRepository: IProductRepository) {}

  async execute(uuid_Store: string): Promise<AProduct[]> {
    try {
      return await this.productRepository.getByUuidStore(uuid_Store);
    } catch (error) {
      if (error instanceof Error) {
        throw new Error(`Error fetching products by store UUID: ${error.message}`);
      }
      throw error;
    }
  }
}
