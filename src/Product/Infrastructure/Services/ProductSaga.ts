// ProductSaga.ts
import { publishToQueue } from './ProductPublisher';

interface SagaStep {
  action: string;
  compensatingAction?: string;
}

const steps: { [key: string]: SagaStep[] } = {
    create: [
      { action: 'createProduct', compensatingAction: 'deleteProduct' },
    ],
    update: [
      { action: 'updateProduct', compensatingAction: 'deleteProduct' },
    ],
  };

export class ProductSaga {
async executeSaga(data: any, type: 'create' | 'update'): Promise<void> {
    for (const step of steps[type]) {
    try {
        await publishToQueue({ data });
    } catch (error) {
        console.error(`Failed to execute step: ${step.action}, compensating: ${step.compensatingAction}`, error);
        await this.rollbackSaga(data, step, type);
        throw error;
    }
    }
}

private async rollbackSaga(data: any, failedStep: SagaStep, type: 'create' | 'update'): Promise<void> {
    const rollbackIndex = steps[type].findIndex(step => step.action === failedStep.action);
    for (let i = rollbackIndex - 1; i >= 0; i--) {
      const compensatingAction = steps[type][i].compensatingAction;
      if (compensatingAction) {
        try {
          await publishToQueue({ data });
        } catch (error) {
          console.error(`Failed to execute compensating action: ${compensatingAction}`, error);
        }
      }
    }
  }
}
