import { Request, Response } from 'express';
import { DeleteProductUseCase } from '../../Application/UseCases/DeleteProductUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';

export class DeleteProductController {
  private deleteProductUseCase: DeleteProductUseCase;

  constructor(private repository: IProductRepository) {
    this.deleteProductUseCase = new DeleteProductUseCase(repository);
  }

  async delete(req: Request, res: Response): Promise<void> {
    try {
      const productId: string = req.params.productId;

      await this.deleteProductUseCase.execute(productId);

      res.status(200).json({ message: 'Product deleted successfully' });
    } catch (error) {
      res.status(500).json({ message: 'Internal Server Error', error});
    }
  }
}
