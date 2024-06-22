// Routes.ts

import express, { Router } from 'express';
import { CreateProductController } from '../Controllers/CreateProductController';
import { DeleteProductController } from '../Controllers/DeleteProductController';
import { ListProductController } from '../Controllers/ListProductController';
import { Repository } from '../Repositories/MysqlRepository';

const router: Router = express.Router();
const repository: Repository = new Repository();

const createProductController: CreateProductController = new CreateProductController(repository);
const deleteProductController: DeleteProductController = new DeleteProductController(repository);
const listProductController: ListProductController = new ListProductController(repository);

// Rutas
router.post('/create-products', async (req, res) => {
  await createProductController.create(req, res);
});

router.get('/products', async (req, res) => {
  await listProductController.list(req, res);
});

router.delete('/products/:productId', async (req, res) => {
  await deleteProductController.delete(req, res);
});

export default router;
