import express, { Router } from 'express';
import { CreateProductController } from '../../Infrastructure/Controllers/CreateProductController';
import { DeleteProductController } from '../../Infrastructure/Controllers/DeleteProductController';
import { ListProductController } from '../../Infrastructure/Controllers/ListProductController';
import { UpdateProductController } from '../../Infrastructure/Controllers/UpdateProductController';
import { GetProductByIdController } from '../../Infrastructure/Controllers/GetProductByIdController';
import { MySQLProductRepository } from '../../Infrastructure/Persistence/MysqlProductRepository';
import { GetProductByUuidStoreController } from '../../Infrastructure/Controllers/GetProductByUuidStoreController';  // Nuevo

const router: Router = express.Router();
const repository = new MySQLProductRepository();

const createProductController = new CreateProductController(repository);
const deleteProductController = new DeleteProductController(repository);
const listProductController = new ListProductController(repository);
const updateProductController = new UpdateProductController(repository);
const getProductByIdController = new GetProductByIdController(repository);
const getProductByUuidStoreController = new GetProductByUuidStoreController(repository);  // Nuevo

// Rutas
router.post('/create-products', async (req, res) => {
  await createProductController.create(req, res);
});

router.delete('/products/:productId', async (req, res) => {
  await deleteProductController.delete(req, res);
});

router.get('/products', async (req, res) => {
  await listProductController.list(req, res);
});

router.put('/products/:productId', async (req, res) => {
  await updateProductController.update(req, res);
});

router.get('/products/:productId', async (req, res) => {
  await getProductByIdController.get(req, res);
});

router.get('/products/store/:uuid_Store', async (req, res) => {
  await getProductByUuidStoreController.get(req, res);  // Nueva ruta
});

export default router;
