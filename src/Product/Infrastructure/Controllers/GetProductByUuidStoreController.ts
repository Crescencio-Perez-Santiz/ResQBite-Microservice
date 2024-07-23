import { Request, Response } from 'express';
import { GetProductByUuidStoreUseCase } from '../../Application/UseCases/GetProductByUuidStoreUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';

export class GetProductByUuidStoreController {
  constructor(private productRepository: IProductRepository) {}

  async get(req: Request, res: Response): Promise<void> {
    const { uuid_Store } = req.params;
    const getProductByUuidStoreUseCase = new GetProductByUuidStoreUseCase(this.productRepository);

    try {
      const products = await getProductByUuidStoreUseCase.execute(uuid_Store);
      res.status(200).json(products);
    } catch (error) {
      if (error instanceof Error) {
        res.status(500).json({ message: error.message });
      } else {
        res.status(500).json({ message: 'Unknown error occurred' });
      }
    }
  }
}
