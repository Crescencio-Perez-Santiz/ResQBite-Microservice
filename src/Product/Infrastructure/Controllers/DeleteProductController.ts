import { Request, Response } from 'express';
import { DeleteProductUseCase } from '../../Application/DeleteProductUseCase';
import { Repository } from '../Repositories/MysqlRepository';

export class DeleteProductController {
  private deleteProductUseCase: DeleteProductUseCase;

  constructor(private repository: Repository) {
    this.deleteProductUseCase = new DeleteProductUseCase(repository);
  }

  async delete(req: Request, res: Response): Promise<void> {
    try {
      const productId: number = parseInt(req.params.productId); // Obtener el ID del producto a eliminar

      await this.deleteProductUseCase.execute(productId);

      res.status(200).json({ message: 'Product deleted successfully' });
    } catch (error) {
      res.status(500).json({ message: 'Internal Server Error', error: error });
    }
  }
}
