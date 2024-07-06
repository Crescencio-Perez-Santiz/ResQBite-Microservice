import { Request, Response } from 'express';
import { GetProductByIdUseCase } from '../../Application/UseCases/GetProductByIdUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';

export class GetProductByIdController {
  private getProductByIdUseCase: GetProductByIdUseCase;

  constructor(private repository: IProductRepository) {
    this.getProductByIdUseCase = new GetProductByIdUseCase(repository);
  }

  async get(req: Request, res: Response): Promise<void> {
    try {
      const productId: string = req.params.productId;

      const result = await this.getProductByIdUseCase.execute(productId);

      if ('error' in result) {
        res.status(404).json({ message: 'Product not found', error: result.error });
      } else {
        res.status(200).json(result);
      }
    } catch (error: any) {
      res.status(500).json({ message: 'Internal Server Error', error: error.toString() });
    }
  }
}
