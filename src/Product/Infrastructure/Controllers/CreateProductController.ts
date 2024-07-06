import { Request, Response } from 'express';
import { CreateProductUseCase } from '../../Application/UseCases/CreateProductUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';
import { Form } from '../../Domain/Entities/Form';

export class CreateProductController {
  private createProductUseCase: CreateProductUseCase;

  constructor(private repository: IProductRepository) {
    this.createProductUseCase = new CreateProductUseCase(repository);
  }

  async create(req: Request, res: Response): Promise<void> {
    try {
      const { name, precio, quantity, sales_description, category, form } = req.body;


      if (!name || !precio || !quantity || !sales_description || !category || !form) {
        throw new Error('Invalid request body');
      }
      
      const productData: AProduct = new AProduct(name, precio, quantity, sales_description, category, new Form(form.description, form.creation_date, form.approximate_expiration_date, form.quality, form.manipulation));
      const result = await this.createProductUseCase.execute(productData);

      if ('error' in result) {
        res.status(400).json({ message: 'Failed to create product', error: result.error });
      } else {
        res.status(201).json({ message: 'Product created successfully', product: result });
      }
    } catch (error:any) {
      res.status(500).json({ message: 'Internal Server Error', error: error.toString() });
    }
  }
}
