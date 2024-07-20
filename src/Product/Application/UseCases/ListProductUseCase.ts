import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';

export class ListProductsUseCase {
  constructor(private repository: IProductRepository) {}

  async execute(): Promise<AProduct[] | { error: string }> {
    try {
      const products = await this.repository.listAll();
      return products;
    } catch (error: any) {
      return { error: error.toString() };
    }
  }
}
