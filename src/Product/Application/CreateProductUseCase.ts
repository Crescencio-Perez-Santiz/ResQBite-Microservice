import { Repository } from '../Infrastructure/Repositories/MysqlRepository';
import { AProduct } from '../Domain/Entities/AProduct';

export class CreateProductUseCase {
  constructor(private repository: Repository) {}

  async execute(productData: AProduct): Promise<[boolean, AProduct | { error: string }]> {
    try {
      // Llamar al método del repositorio para guardar el producto
      const product = await this.repository.save(productData);
      
      // Si el producto se guardó correctamente, devolver éxito y el producto creado
      return [true, product];
    } catch (error: any) { // Aquí se especifica el tipo 'any' para 'error'
      // Si hay algún error al guardar el producto, devolver error
      return [false, { error: error.toString() }];
    }
  }
}
