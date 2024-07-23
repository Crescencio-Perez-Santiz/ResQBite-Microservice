import { AProduct } from '../Entities/AProduct';

export interface IProductRepository {
  save(product: AProduct): Promise<AProduct>;
  listAll(): Promise<AProduct[]>;
  get_by_id(id: string): Promise<AProduct | null>;
  delete(product_uuid: string): Promise<void>;
  update(productId: string, productData: Partial<AProduct>): Promise<AProduct>;

  getByUuidStore(uuid_Store: string): Promise<AProduct[]>;

}
