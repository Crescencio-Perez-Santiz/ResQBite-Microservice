import { AProduct } from '../Entities/AProduct';

export interface IProductRepository {
  save(product: AProduct): Promise<AProduct>;
  listAll(): Promise<AProduct[]>;
  get_by_id(id: string): Promise<AProduct | null>;
  delete(id: string): Promise<void>;
  update(productId: string, productData: Partial<AProduct>): Promise<AProduct>;
}
