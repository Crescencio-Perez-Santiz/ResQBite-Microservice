
import { Request, Response } from 'express';
import { UpdateProductUseCase } from '../../Application/UseCases/UpdateProductUseCase';
import { IProductRepository } from '../../Domain/Repositories/IProductRepository';
import { AProduct } from '../../Domain/Entities/AProduct';
import { Form } from '../../Domain/Entities/Form';
import { s3 } from '../Config/awsConfig';
import multer from 'multer';
import multerS3 from 'multer-s3';
import { ProductSaga } from '../Services/ProductSaga';

import { classifyText } from '../NPL/TextClassifier_Grosery';
import { containsNonFoodWords } from '../NPL/TextClassifier_nonFood';

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
  private productSaga: ProductSaga;

  constructor(private repository: IProductRepository) {
    this.updateProductUseCase = new UpdateProductUseCase(repository);
    this.productSaga = new ProductSaga();
  }

  async update(req: Request, res: Response): Promise<void> {
    try {
      upload(req, res, async (uploadError: any) => {
        if (uploadError) {
          return res.status(500).json({ message: 'Error uploading file', error: uploadError.toString() });
        }

        const productId: string = req.params.productId;
        const { name, precio, quantity, sales_description, category, form, uuid_Store } = req.body;
        const image = (req.file as Express.MulterS3.File)?.location;

        if (!name || !precio || !quantity || !sales_description || !category || !image || !uuid_Store) {
          return res.status(400).json({ message: 'Invalid request body' });
        }

        // Verificar que no se hable de objetos
        const nameHasNonFoodWords = containsNonFoodWords(name);
        const sales_descriptionHasNonFoodWords = containsNonFoodWords(sales_description);
        const descriptionHasNonFoodWords = containsNonFoodWords(form.description);

        if (descriptionHasNonFoodWords || nameHasNonFoodWords || sales_descriptionHasNonFoodWords) {
          return res.status(400).json({ message: 'No se encontro relación con comida' });
        }


        // Verificar lenguaje inapropiado en formulario
        const descriptionStatus = classifyText(form.description);
        const qualityStatus = classifyText(form.quality);
        const manipulationStatus = classifyText(form.manipulation);

        if (descriptionStatus === "El texto contiene lenguaje inapropiado." || 
            qualityStatus === "El texto contiene lenguaje inapropiado." || 
            manipulationStatus === "El texto contiene lenguaje inapropiado.") {
          return res.status(400).json({ message: 'Lenguaje inapropiado en el formulario' });
        }

        const productData: Partial<AProduct> = {
          name,
          precio,
          quantity,
          sales_description,
          category,
          form: new Form(form.description, form.creation_date, form.approximate_expiration_date, form.quality, form.manipulation),
          uuid_Store,
          image 
        };

        const result = await this.updateProductUseCase.execute(productId, productData);

        if ('error' in result) {
          res.status(404).json({ message: 'Failed to update product', error: result.error });
        } else {
          try {
            const message = { action: 'updateProduct', productData: result };
            console.log('Publishing message to queue:', message);
            await this.productSaga.executeSaga(message, 'update');
            res.status(200).json({ message: 'Product updated successfully and saga executed', product: result });
          } catch (sagaError) {
            res.status(500).json({ message: 'Saga execution failed', error: (sagaError as Error).toString() });
          }
        }
      });
    } catch (error) {
      res.status(500).json({ message: 'Internal Server Error', error: (error as Error).toString() });
    }
  }
}
