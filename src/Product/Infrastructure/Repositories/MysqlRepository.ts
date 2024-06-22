import { getRepository } from 'typeorm';
import { ProductModel } from '../../../Database/mysqlConection';
import { AProduct as ProductDomain } from '../../Domain/Entities/AProduct';


export class Repository {
    private productRepository = getRepository(ProductModel);

    async save(productDomain: ProductDomain): Promise<ProductModel> {
        const product = this.productRepository.create({
            product_uuid: productDomain.product_uuid,
            name: productDomain.name,
            precio: productDomain.precio,
            stock: productDomain.stock,
        });

        return await this.productRepository.save(product);
    }

    async list_all(): Promise<ProductModel[]> {
        return await this.productRepository.find();
    }

    async get_by_id(id: number): Promise<ProductModel | undefined> {
        const product = await this.productRepository.findOne({ where: { id } });
        return product || undefined; // Convertir null a undefined
    }
    

    async getByUuid(product_uuid: string): Promise<ProductModel | undefined> {
        const product = await this.productRepository.findOne({ where: { product_uuid } });
        return product || undefined; // Convertir null a undefined
    }

    async delete(id: number): Promise<void> {
        const product = await this.get_by_id(id);
        if (product) {
            await this.productRepository.delete(id);
        }
    }
}
