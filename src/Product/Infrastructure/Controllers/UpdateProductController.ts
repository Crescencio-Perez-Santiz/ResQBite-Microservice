import { Request, Response } from 'express';
import { UpdateProductUseCase } from '../../Application/UseCases/UpdateProductUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';

export class UpdateProductController {
  private updateProductUseCase: UpdateProductUseCase;

  constructor(private repository: IProductRepository) {
    this.updateProductUseCase = new UpdateProductUseCase(repository);
  }

  async update(req: Request, res: Response): Promise<void> {
    try {
      const productId: string = req.params.productId;
      const productData: Partial<AProduct> = req.body;

      const result = await this.updateProductUseCase.execute(productId, productData);

      if ('error' in result) {
        res.status(404).json({ message: 'Product not found', error: result.error });
      } else {
        res.status(200).json({ message: 'Product updated successfully', product: result });
      }
    } catch (error: any) {
      res.status(500).json({ message: 'Internal Server Error', error: error.toString() });
    }
  }
}
