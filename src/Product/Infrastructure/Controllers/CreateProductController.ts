import { Request, Response } from 'express';
import { CreateProductUseCase } from '../../Application/UseCases/CreateProductUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';
import { Form } from '../../Domain/Entities/Form';
import { s3 } from '../Config/awsConfig';
import multer from 'multer';
import multerS3 from 'multer-s3';

const upload = multer({
  storage: multerS3({
    s3, 
    bucket: process.env.AWS_S3_BUCKET_NAME!,
    acl: 'public-read',
    metadata: function (req, file, cb) {
      cb(null, { fieldName: file.fieldname });
    },
    key: function (req, file, cb) {
      cb(null, Date.now().toString() + file.originalname);
    }
  })
}).single('image');

export class CreateProductController {
  private createProductUseCase: CreateProductUseCase;

  constructor(private repository: IProductRepository) {
    this.createProductUseCase = new CreateProductUseCase(repository);
  }

  async create(req: Request, res: Response): Promise<void> {
    upload(req, res, async (error: any) => {
      if (error) {
        return res.status(500).json({ message: 'Error uploading file', error: error.toString() });
      }

      const { name, precio, quantity, sales_description, category, form} = req.body;
      const image = (req.file as Express.MulterS3.File).location; // URL de la imagen en S3

      if (!name || !precio || !quantity || !sales_description || !category || !image) {
        return res.status(400).json({ message: 'Invalid request body' });
      }

      const productData: AProduct = new AProduct(
        name,
        precio,
        quantity,
        sales_description,
        category,
        new Form(form.description, form.creation_date, form.approximate_expiration_date, form.quality, form.manipulation),
        image // Añadimos la URL de la imagen aquí
      );

      const result = await this.createProductUseCase.execute(productData);

      if ('error' in result) {
        res.status(400).json({ message: 'Failed to create product', error: result.error });
      } else {
        res.status(201).json({ message: 'Product created successfully', product: result });
      }
    });
  }
}
