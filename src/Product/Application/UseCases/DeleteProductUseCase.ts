import { IProductRepository } from '../../Domain/Repositories/IProductRepository';

export class DeleteProductUseCase {
  constructor(private repository: IProductRepository) {}

  async execute(productId: string): Promise<void | { error: string }> {
    try {
      await this.repository.delete(productId);
    } catch (error:any) {
      return { error: error.toString() };
    }
  }
}
