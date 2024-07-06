import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';

export class ListProductsUseCase {
  constructor(private repository: IProductRepository) {}

  async execute(): Promise<AProduct[]> {
    return await this.repository.listAll();
  }
}
