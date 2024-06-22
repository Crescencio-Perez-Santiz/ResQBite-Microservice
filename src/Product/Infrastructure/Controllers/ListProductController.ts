// ListProductController.ts

import { Request, Response } from 'express';
import { ListProductUseCase } from '../../Application/ListProductUseCase';
import { Repository } from '../Repositories/MysqlRepository';

export class ListProductController {
  private listProductUseCase: ListProductUseCase;

  constructor(private repository: Repository) {
    this.listProductUseCase = new ListProductUseCase(repository);
  }

  async list(req: Request, res: Response): Promise<void> {
    try {
      const products = await this.listProductUseCase.execute();
      res.status(200).json({ products }); // Devolver los productos en un objeto JSON
    } catch (error) {
      console.error('Error al obtener la lista de productos:', error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
}
