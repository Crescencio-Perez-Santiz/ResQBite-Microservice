import { Request, Response } from 'express';
import { DeleteProductUseCase } from '../../Application/UseCases/DeleteProductUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { publishToQueue } from '../../Infrastructure/Services/ProductPublisher';

export class DeleteProductController {
  private deleteProductUseCase: DeleteProductUseCase;

  constructor(private repository: IProductRepository) {
    this.deleteProductUseCase = new DeleteProductUseCase(repository);
  }

  async delete(req: Request, res: Response): Promise<void> {
    try {
      const productId: string = req.params.productId;

      const result = await this.deleteProductUseCase.execute(productId);

      if (result && 'error' in result) {
        res.status(400).json({ message: 'Failed to delete product', error: result.error });
      } else {
        const message = { action: 'delete', productId };
        console.log('Publishing message to queue:', message);
        await publishToQueue(message);
        res.status(200).json({ message: 'Product deleted successfully and message sent to queue' });
      }
    } catch (error: any) {
      res.status(500).json({ message: 'Internal Server Error', error: error.toString() });
    }
  }
}
