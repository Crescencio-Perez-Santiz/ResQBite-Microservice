import { Request, Response } from 'express';
import { UpdateProductUseCase } from '../../Application/UseCases/UpdateProductUseCase';
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

export class UpdateProductController {
  private updateProductUseCase: UpdateProductUseCase;

  constructor(private repository: IProductRepository) {
    this.updateProductUseCase = new UpdateProductUseCase(repository);
  }

  async update(req: Request, res: Response): Promise<void> {
    upload(req, res, async (error: any) => {
      if (error) {
        return res.status(500).json({ message: 'Error uploading file', error: error.toString() });
      }

      const productId: string = req.params.productId;
      const { name, precio, quantity, sales_description, category, form } = req.body;
      const image = (req.file as Express.MulterS3.File)?.location; // URL de la imagen en S3

      if (!name || !precio || !quantity || !sales_description || !category) {
        return res.status(400).json({ message: 'Invalid request body' });
      }

      const productData: Partial<AProduct> = {
        name,
        precio,
        quantity,
        sales_description,
        category,
        form: new Form(form.description, form.creation_date, form.approximate_expiration_date, form.quality, form.manipulation),
        image // Actualiza la URL de la imagen solo si se proporciona una nueva imagen
      };

      const result = await this.updateProductUseCase.execute(productId, productData);

      if ('error' in result) {
        res.status(404).json({ message: 'Product not found', error: result.error });
      } else {
        res.status(200).json({ message: 'Product updated successfully', product: result });
      }
    });
  }
}
