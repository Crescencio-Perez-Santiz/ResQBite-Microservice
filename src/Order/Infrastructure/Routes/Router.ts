import { Router } from "express";
import { createOrderController } from "../Controllers/CreateOrderController";

const router = Router();

router.post("/orders", createOrderController);

export default router;
