import { Request, Response } from 'express';
import { ListProductsUseCase } from '../../Application/UseCases/ListProductUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';

export class ListProductController {
  private listProductsUseCase: ListProductsUseCase;

  constructor(private repository: IProductRepository) {
    this.listProductsUseCase = new ListProductsUseCase(repository);
  }

  async list(req: Request, res: Response): Promise<void> {
    try {
      const products = await this.listProductsUseCase.execute();
      res.status(200).json(products);
    } catch (error) {
      res.status(500).json({ message: 'Internal Server Error', error});
    }
  }
}
