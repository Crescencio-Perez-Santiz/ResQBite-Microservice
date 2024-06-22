import { Request, Response } from 'express';
import { CreateProductUseCase } from '../../Application/CreateProductUseCase';
import { AProduct } from '../../Domain/Entities/AProduct';
import { Repository } from '../Repositories/MysqlRepository';

export class CreateProductController {
  private createProductUseCase: CreateProductUseCase;

  constructor(private repository: Repository) {
    this.createProductUseCase = new CreateProductUseCase(repository);
  }

  async create(req: Request, res: Response): Promise<void> {
    try {
      // Verificar si req.body está definido y contiene las propiedades necesarias
      if (!req.body || !req.body.name || !req.body.precio || !req.body.stock) {
        throw new Error('Invalid request body');
      }
  
      // Extraer los datos del cuerpo de la solicitud
      const { name, precio, stock } = req.body;
  
      // Crear una instancia de AProduct con los datos proporcionados
      const productData: AProduct = new AProduct(name, precio, stock);
  
      // Llamar al caso de uso para crear el producto
      const [success, result] = await this.createProductUseCase.execute(productData);
  
      // Comprobar si el producto se creó exitosamente
      if (success) {
        res.status(201).json({ message: 'Product created successfully', product: result });
      } else {
        res.status(400).json({ message: 'Failed to create product', error: result });
      }
    } catch (error) {
      res.status(500).json({ message: 'Internal Server Error', error: error});
    }
  }
  
  
}
