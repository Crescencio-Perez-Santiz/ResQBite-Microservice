// ListProductUseCase.ts

import { Repository } from '../Infrastructure/Repositories/MysqlRepository';
import { ProductModel } from '../../Database/mysqlConection';

export class ListProductUseCase {
  constructor(private repository: Repository) {}

  async execute(): Promise<ProductModel[]> {
    return this.repository.list_all();
  }
}
