import { IProductRepository } from '../../Domain/Repositories/IProductRepository';

export class DeleteProductUseCase {
  constructor(private repository: IProductRepository) {}

  async execute(productId: string): Promise<void> {
    await this.repository.delete(productId);
  }
}
