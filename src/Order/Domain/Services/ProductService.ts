import { getRepository } from "typeorm";
import { ProductModel } from "../../Infrastructure/Repositories/Models/ProductModel";

export const handleProductCreationOrUpdate = async (productData: any) => {
    const productRepository = getRepository(ProductModel);

    // Asegúrate de que los datos del producto tienen todos los campos necesarios
    if (!productData.product_uuid || !productData.uuid_Store) {
        console.error(
            "Faltan datos necesarios del producto: product_uuid o uuid_Store"
        );
        return;
    }

    const existingProduct = await productRepository.findOne({
        where: { product_uuid: productData.product_uuid },
    });

    if (existingProduct) {
        existingProduct.store_uuid = productData.uuid_Store;
        existingProduct.quantity = productData.quantity;
        existingProduct.price = productData.precio;
        existingProduct.name = productData.name;
        existingProduct.description = productData.sales_description;
        existingProduct.category = productData.category;
        existingProduct.image_url = productData.image;
        existingProduct.updated_at = new Date();
        await productRepository.save(existingProduct);
        console.log(
            `Producto ${existingProduct.product_uuid} actualizado con nuevo stock: ${existingProduct.quantity}`
        );
    } else {
        const newProduct = productRepository.create({
            product_uuid: productData.product_uuid,
            store_uuid: productData.uuid_Store,
            name: productData.name,
            price: productData.precio,
            quantity: productData.quantity,
            description: productData.sales_description,
            category: productData.category,
            image_url: productData.image,
            created_at: new Date(),
            updated_at: new Date(),
        });
        await productRepository.save(newProduct);
        console.log(
            `Producto ${newProduct.product_uuid} creado con stock: ${newProduct.quantity}`
        );
    }
};

export const deleteProduct = async (productId: string) => {
    const productRepository = getRepository(ProductModel);

    console.log(`Intentando eliminar producto con UUID: ${productId}`);

    // Verificar si el producto existe antes de eliminar
    const product = await productRepository.findOne({
        where: { product_uuid: productId },
    });

    if (!product) {
        console.log(`Producto ${productId} no encontrado para eliminación`);
        return;
    }

    console.log(`Producto encontrado: ${JSON.stringify(product)}`);

    // Proceder con la eliminación
    const deleteResult = await productRepository.delete({
        product_uuid: productId,
    });

    if (deleteResult.affected === 1) {
        console.log(`Producto ${productId} eliminado`);
    } else {
        console.log(`Producto ${productId} no encontrado para eliminación`);
    }
};
