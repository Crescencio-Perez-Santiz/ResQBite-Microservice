import { Repository } from '../Infrastructure/Repositories/MysqlRepository';

export class DeleteProductUseCase {
  constructor(private repository: Repository) {}

  async execute(productId: number): Promise<void> {
    await this.repository.delete(productId);
  }
}
